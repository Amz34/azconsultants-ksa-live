/* Invertio Advisory — site behaviour: mobile navigation + tender board rendering.
   No dependencies. Tender data comes from tenders-data.js (window.TENDER_FEED). */
(function () {
  'use strict';

  /* ---------- mobile navigation ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ---------- tender board ---------- */
  var board = document.getElementById('board');
  var grids = board ? board.querySelectorAll('[data-board-section]') : [];
  if (!grids.length || !window.TENDER_FEED) { return; }

  var feed = window.TENDER_FEED;
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  function parseStamp(value) {
    if (!value) { return null; }
    var m = String(value).trim().match(/^(\d{4})-(\d{2})-(\d{2})(?:[\sT]+(\d{2}):(\d{2}))?/);
    if (!m) { return null; }
    return new Date(
      Number(m[1]), Number(m[2]) - 1, Number(m[3]),
      m[4] ? Number(m[4]) : 23, m[5] ? Number(m[5]) : 59
    );
  }

  function fmt(date) {
    if (!date) { return '—'; }
    var hh = String(date.getHours()).padStart(2, '0');
    var mm = String(date.getMinutes()).padStart(2, '0');
    return date.getDate() + ' ' + MONTHS[date.getMonth()] + ' ' + date.getFullYear() + ', ' + hh + ':' + mm;
  }

  function fmtDay(date) {
    if (!date) { return '—'; }
    return date.getDate() + ' ' + MONTHS[date.getMonth()] + ' ' + date.getFullYear();
  }

  var now = new Date();
  var DAY = 86400000;

  var rows = feed.tenders.map(function (t) {
    var close = parseStamp(t.offersClose);
    var days = close ? Math.ceil((close - now) / DAY) : null;
    var state = 'open';
    var stateLabel = 'Open';
    if (close && close < now) {
      state = 'expired';
      stateLabel = 'Expired ' + fmtDay(close);
    } else if (days !== null && days <= 7) {
      state = 'closing';
      stateLabel = days <= 0 ? 'Closes today' : 'Closes in ' + days + ' day' + (days === 1 ? '' : 's');
    }
    return {
      raw: t,
      close: close,
      days: days,
      state: state,
      stateLabel: stateLabel,
      isIt: /information technology/i.test(t.activityEn)
    };
  });

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) { node.className = className; }
    if (text !== undefined && text !== null && text !== '') { node.textContent = text; }
    return node;
  }

  function metaRow(label, value) {
    var wrap = el('div');
    wrap.appendChild(el('dt', null, label));
    wrap.appendChild(el('dd', null, value || '—'));
    return wrap;
  }

  function addMeta(meta, label, value) {
    if (value) { meta.appendChild(metaRow(label, value)); }
  }

  function card(row) {
    var t = row.raw;
    var article = el('article', 'card' + (t.featured ? ' card-featured' : ''));

    var top = el('div', 'card-top');
    top.appendChild(el('span', 'badge badge-' + row.state, row.stateLabel));
    top.appendChild(el('span', 'badge', t.type));
    if (t.sectorEn) {
      top.appendChild(el('span', 'badge badge-sector', t.sectorEn));
    }
    if (t.featured) { top.appendChild(el('span', 'badge badge-feat', 'Picked for our service lines')); }
    article.appendChild(top);

    article.appendChild(el('h3', null, t.titleEn || t.titleAr));
    var ar = el('p', 'title-ar ar', t.titleAr);
    article.appendChild(ar);

    var meta = el('dl', 'meta');
    meta.appendChild(metaRow('Entity', t.entity));
    meta.appendChild(metaRow('Activity', t.activityEn));
    meta.appendChild(metaRow('Reference number', t.ref));
    meta.appendChild(metaRow('Competition number', t.compNo === 'لا يوجد' ? 'Not applicable' : t.compNo));
    meta.appendChild(metaRow('Published', t.published));
    meta.appendChild(metaRow('Enquiries close', t.inquiryClose));
    meta.appendChild(metaRow('Offers close', fmt(row.close)));
    meta.appendChild(metaRow('Offers open', t.offersOpen ? fmt(parseStamp(t.offersOpen)) : 'Not published'));
    addMeta(meta, 'Tender documents value (SAR)', t.fee === 'مجانا' ? 'Free' : t.fee);
    addMeta(meta, 'Contract duration', t.duration);
    article.appendChild(meta);

    if (t.scopeEn) { article.appendChild(el('p', 'scope', t.scopeEn)); }

    var foot = el('div', 'foot');
    var refWrap = el('div', 'card-actions');
    refWrap.appendChild(el('span', 'ref', 'Ref ' + t.ref));

    var copyBtn = el('button', 'btn-action', 'Copy Ref');
    copyBtn.type = 'button';
    copyBtn.setAttribute('aria-label', 'Copy reference number ' + t.ref);
    copyBtn.addEventListener('click', function (e) {
      e.preventDefault();
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(t.ref);
      } else {
        var ta = document.createElement('textarea');
        ta.value = t.ref;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
      }
      copyBtn.textContent = 'Copied!';
      setTimeout(function () { copyBtn.textContent = 'Copy Ref'; }, 2000);
    });
    refWrap.appendChild(copyBtn);

    var waLink = el('a', 'btn-action btn-wa-card', 'Enquire');
    var waMsg = encodeURIComponent('Hello, I would like to consult on Tender Ref ' + t.ref + ' (' + (t.titleEn || t.titleAr) + ').');
    waLink.href = 'https://wa.me/966574268856?text=' + waMsg;
    waLink.target = '_blank';
    waLink.rel = 'noopener';
    refWrap.appendChild(waLink);

    foot.appendChild(refWrap);

    var link = el('a', 'arrow', 'Official tender page on Etimad \u2197');
    link.href = String(t.link || "").trim().replace(/\s+/g, "%20");
    link.rel = 'noopener';
    link.target = '_blank';
    foot.appendChild(link);
    article.appendChild(foot);

    return article;
  }

  var activeQuery = '';

  function matches(row, filter) {
    if (filter === 'open' && row.state === 'expired') { return false; }
    if (filter === 'closing' && row.state !== 'closing') { return false; }
    if (filter === 'expired' && row.state !== 'expired') { return false; }
    if (filter === 'it' && !row.isIt) { return false; }
    if (filter === 'featured' && !row.raw.featured) { return false; }
    if (filter === 'utilities_fm' && (row.raw.sectorKey !== 'utilities_fm' && !row.raw.sectorKey)) { return false; }
    if (filter === 'tech' && (row.raw.sectorKey !== 'tech' && !row.isIt)) { return false; }
    if (filter === 'construction' && row.raw.sectorKey !== 'construction') { return false; }
    if (filter === 'consultancy' && row.raw.sectorKey !== 'consultancy') { return false; }
    if (filter === 'supply' && row.raw.sectorKey !== 'supply') { return false; }

    if (activeQuery) {
      var t = row.raw;
      var haystack = [
        t.titleEn || '',
        t.titleAr || '',
        t.entity || '',
        t.entityAr || '',
        t.activityEn || '',
        t.activityAr || '',
        t.ref || '',
        t.compNo || '',
        t.scopeEn || ''
      ].join(' ').toLowerCase();
      if (haystack.indexOf(activeQuery) === -1) {
        return false;
      }
    }
    return true;
  }

  var sorted = rows.slice().sort(function (a, b) {
    if (!a.close) { return 1; }
    if (!b.close) { return -1; }
    return a.close - b.close;
  });

  var captured = document.getElementById('board-captured');
  if (captured) { captured.textContent = 'Captured: ' + (feed.capturedAt || '—'); }
  var countEl = document.getElementById('board-count');

  var emptyEl = el('div', 'board-empty-wrap');
  var emptyMsg = el('p', 'muted', 'No tenders match this filter or keyword in the current reading.');
  var emptyResetBtn = el('button', 'chip', 'Reset Search & Filters');
  emptyResetBtn.type = 'button';
  emptyResetBtn.style.marginTop = '10px';
  emptyResetBtn.addEventListener('click', function () {
    activeQuery = '';
    activeFilter = 'open';
    var searchInput = document.getElementById('tender-search');
    if (searchInput) { searchInput.value = ''; }
    var clearBtn = document.getElementById('tender-search-clear');
    if (clearBtn) { clearBtn.style.display = 'none'; }
    var chips = document.querySelectorAll('#board-filters .chip');
    Array.prototype.forEach.call(chips, function (chip) {
      chip.setAttribute('aria-pressed', chip.getAttribute('data-filter') === 'open' ? 'true' : 'false');
    });
    render('open');
  });
  emptyEl.appendChild(emptyMsg);
  emptyEl.appendChild(emptyResetBtn);
  emptyEl.id = 'board-empty';
  emptyEl.hidden = true;
  board.appendChild(emptyEl);

  function render(filter) {
    var shown = 0;
    Array.prototype.forEach.call(grids, function (grid) {
      var key = grid.getAttribute('data-board-section');
      var block = grid.closest('.board-sec');
      var n = 0;
      grid.innerHTML = '';
      sorted.forEach(function (row) {
        if ((row.raw.section || 'services') !== key) { return; }
        if (!matches(row, filter)) { return; }
        grid.appendChild(card(row));
        n += 1;
      });
      shown += n;
      if (block) { block.hidden = n === 0; }
      var badge = document.querySelector('[data-sec-n="' + key + '"]');
      if (badge) { badge.textContent = n ? n + ' listed' : ''; }
    });
    emptyEl.hidden = shown > 0;
    if (countEl) { countEl.textContent = 'Showing ' + shown + ' of ' + feed.count + ' tenders'; }
  }

  var activeFilter = 'all';
  var chips = document.querySelectorAll('#board-filters .chip');
  Array.prototype.forEach.call(chips, function (chip) {
    chip.addEventListener('click', function () {
      Array.prototype.forEach.call(chips, function (other) {
        other.setAttribute('aria-pressed', other === chip ? 'true' : 'false');
      });
      activeFilter = chip.getAttribute('data-filter');
      render(activeFilter);
    });
  });

  var searchInput = document.getElementById('tender-search');
  var clearBtn = document.getElementById('tender-search-clear');
  if (searchInput) {
    searchInput.addEventListener('input', function () {
      activeQuery = String(searchInput.value || '').trim().toLowerCase();
      if (clearBtn) {
        clearBtn.style.display = activeQuery ? 'inline-block' : 'none';
      }
      render(activeFilter);
    });
  }
  if (clearBtn && searchInput) {
    clearBtn.addEventListener('click', function () {
      searchInput.value = '';
      activeQuery = '';
      clearBtn.style.display = 'none';
      render(activeFilter);
      searchInput.focus();
    });
  }

  var defaultChip = document.querySelector('#board-filters [data-filter="open"]');
  if (defaultChip) {
    var allChips = document.querySelectorAll('#board-filters .chip');
    Array.prototype.forEach.call(allChips, function (c) { c.setAttribute('aria-pressed', c === defaultChip ? 'true' : 'false'); });
    activeFilter = 'open';
    render('open');
  } else {
    render('all');
  }
}());

/* enquiry form: honest notice when the server-side handoff fails (no silent lead loss) */
(function () {
  if (!/[?&]err=/.test(location.search)) return;
  var form = document.querySelector('form.enquiry');
  if (!form) return;
  var p = document.createElement('p');
  p.className = 'form-notice';
  p.setAttribute('role', 'alert');
  p.textContent = (document.documentElement.lang === 'ar')
    ? 'عذرًا، لم يتم إرسال الطلب. الرجاء المحاولة مرة أخرى، أو التواصل معنا مباشرة عبر واتساب أو الاتصال.'
    : 'Sorry - that did not go through. Please try again, or reach us directly on WhatsApp or by phone.';
  form.parentNode.insertBefore(p, form);
}());
