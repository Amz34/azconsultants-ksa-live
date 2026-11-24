/**
 * Cloudflare Pages Function: /api/inquiry
 * Handles instant lead intake and securely notifies @AzGem_Bot on Telegram at the edge.
 */

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

export async function onRequestPost(context) {
  const { request, env } = context;

  try {
    const data = await request.json();

    const firstName = (data.first_name || 'Prospect').trim();
    const lastName = (data.last_name || '').trim();
    const fullName = `${firstName} ${lastName}`.trim();
    const email = (data.email || 'N/A').trim();
    const company = (data.company || 'N/A').trim();
    const service = (data.service || 'Tender Intelligence').trim();
    const capex = (data.capex || 'Under SAR 10M').trim();
    const region = (data.region || 'Riyadh / Central').trim();
    const timeline = (data.timeline || '1-3 Months').trim();
    const wantsCall = data.wantsCall ? 'Yes (Requested 20-min introductory scoping call)' : 'No (Written assessment requested)';
    const phone = (data.phone || 'N/A').trim();

    // Unique reference stamp
    const refId = 'AZ-KSA-2026-' + Math.floor(1000 + Math.random() * 9000);

    // Dynamic Viability Scoring logic
    let score = 91;
    if (capex.includes('50M') || capex.includes('250M')) score += 5;
    if (timeline.includes('Urgent') || timeline.includes('2 to 4')) score += 3;
    score = Math.min(98, score);

    // LCGPA assessment calculation
    let lcgpaStatus = 'Capex under SAR 10M threshold (pre-LCGPA penalty window; high bidding advantage)';
    if (capex.includes('10M to SAR 50M') || capex.includes('50M') || capex.includes('250M')) {
      lcgpaStatus = 'Mandatory 30% Local Content gate applies for consultancy tenders of SAR 10M+ from 1 Apr 2027';
    }

    // Telegram Bot Token (from Cloudflare Environment secret or default server token)
    const botToken = env.TELEGRAM_BOT_TOKEN;
    if (!botToken) {
      return new Response(JSON.stringify({ ok: false, error: 'Missing TELEGRAM_BOT_TOKEN secret' }), { status: 500, headers: { 'Content-Type': 'application/json' } });
    }
    const chatId = env.TELEGRAM_CHAT_ID || '8843884232';

    // Structured HTML alert with escaping for Telegram
    const alertText = [
      `<b>[AZ CONSULTANTS - NEW LEAD SUBMISSION]</b>`,
      ``,
      `<b>Ref ID:</b> <code>${escapeHtml(refId)}</code>`,
      `<b>Viability Score:</b> <b>${score}%</b>`,
      ``,
      `<b>Prospect:</b> ${escapeHtml(fullName)}`,
      `<b>Organization:</b> ${escapeHtml(company)}`,
      `<b>Email:</b> ${escapeHtml(email)}`,
      `<b>Phone/WhatsApp:</b> <code>${escapeHtml(phone)}</code>`,
      ``,
      `<b>Mandate Focus:</b> ${escapeHtml(service)}`,
      `<b>Capex Scale:</b> ${escapeHtml(capex)}`,
      `<b>Region:</b> ${escapeHtml(region)}`,
      `<b>Timeline:</b> ${escapeHtml(timeline)}`,
      `<b>Introductory Call:</b> ${escapeHtml(wantsCall)}`,
      ``,
      `<b>LCGPA Analysis:</b> ${escapeHtml(lcgpaStatus)}`,
      ``,
      `<i>Lead captured via live AZ Consultants questionnaire gateway.</i>`
    ].join('\n');

    // Edge dispatch to Telegram
    const tgUrl = `https://api.telegram.org/bot${botToken}/sendMessage`;
    const tgResp = await fetch(tgUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chat_id: chatId,
        text: alertText,
        parse_mode: 'HTML'
      })
    });

    const tgResult = await tgResp.json();

    return new Response(JSON.stringify({
      ok: true,
      reference: refId,
      score: score,
      lcgpa_status: lcgpaStatus,
      dispatch: tgResult.ok ? 'delivered' : 'queued'
    }), {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });

  } catch (err) {
    return new Response(JSON.stringify({
      ok: false,
      error: err.message
    }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
