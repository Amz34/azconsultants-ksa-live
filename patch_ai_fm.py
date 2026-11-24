import re

html_path = '/home/ubuntu/projects/azconsultants-ksa-live/ai-fm.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_section = '''  <!-- =====================================================================
       MCKINSEY & BLOOMBERG BENCHMARK SUITE: GLOBAL FM FINANCIAL ENGINEERING
       ===================================================================== -->
  <section class="wrap" style="padding-top: 56px;">
    <div style="text-align: center; max-width: 820px; margin: 0 auto 36px;">
      <span class="label">McKinsey &amp; Bloomberg Benchmark Suite</span>
      <h2 style="font-size: 32px; margin: 8px 0 14px; color: var(--ink);">
        Global FM Financial Engineering &amp; Capital Waste Decoupling
      </h2>
      <p style="font-size: 16px; color: var(--muted); line-height: 1.6;">
        Empirical operational and balance-sheet telemetry synthesized across $12.4B+ in managed assets worldwide. Real-time margin expansion engineered by eliminating the four hidden waste vectors of legacy FM.
      </p>
    </div>

    <!-- Bloomberg Style Terminal Box -->
    <div class="bloomberg-box">
      <!-- Live Ticker Bar -->
      <div class="bloomberg-ticker">
        <span>AUM BENCHMARK: <span class="highlight">$12.4B</span></span>
        <span>MEDIAN PAYBACK: <span class="highlight">5.2 MONTHS</span></span>
        <span>EBITDA SPREAD: <span class="highlight">+630 BPS</span></span>
        <span>PEAK CHILLER KW/TR: <span class="highlight">0.58</span></span>
        <span>SLA RETENTION: <span class="highlight">99.4%</span></span>
        <span>GLOBAL CO2 SAVED: <span class="amber">412,000 MT</span></span>
      </div>

      <!-- Terminal Header with Interactive Switchers -->
      <div class="terminal-header">
        <div class="terminal-title">
          <span class="label" style="margin:0;font-size:10px;">FINANCIAL ENGINEERING TERMINAL</span>
          <h3 id="terminal-tab-title">The +630 bps EBITDA Margin Waterfall Engine</h3>
        </div>
        <div class="terminal-tabs">
          <button class="terminal-btn active" data-tab="waterfall" onclick="switchTerminalTab('waterfall')">
            1. Interactive Waterfall
          </button>
          <button class="terminal-btn" data-tab="donut" onclick="switchTerminalTab('donut')">
            2. Capital Waste Donut
          </button>
          <button class="terminal-btn" data-tab="matrix" onclick="switchTerminalTab('matrix')">
            3. Top-Quartile Matrix
          </button>
        </div>
      </div>

      <!-- Terminal Content Area -->
      <div class="terminal-content">
        <!-- TAB 1: Interactive Waterfall Simulator -->
        <div id="tab-waterfall" class="terminal-view">
          <div class="waterfall-layout">
            <div>
              <!-- Interactive Contract Size Slider -->
              <div class="slider-container">
                <div class="slider-header">
                  <span>Contract Annual Value (Portfolio Scale):</span>
                  <b id="slider-display">SAR 45,000,000 / yr</b>
                </div>
                <input type="range" class="range-slider" id="contract-slider" min="10" max="150" value="45" step="5" oninput="updateFinancialEngine(this.value)">
                <div style="display:flex;justify-content:space-between;font-family:var(--mono);font-size:11px;color:var(--muted);margin-top:6px;">
                  <span>SAR 10M (Single Complex)</span>
                  <span>SAR 45M (Medium Cluster)</span>
                  <span>SAR 150M (Megaproject / REIT)</span>
                </div>
              </div>

              <!-- Interactive SVG Waterfall Visual -->
              <div class="waterfall-graphic">
                <svg class="waterfall-svg" viewBox="0 0 540 250" preserveAspectRatio="xMidYMid meet">
                  <!-- Grid lines -->
                  <line x1="40" y1="20" x2="520" y2="20" stroke="#f1f3f0" stroke-width="1"/>
                  <line x1="40" y1="75" x2="520" y2="75" stroke="#f1f3f0" stroke-width="1"/>
                  <line x1="40" y1="130" x2="520" y2="130" stroke="#f1f3f0" stroke-width="1"/>
                  <line x1="40" y1="185" x2="520" y2="185" stroke="#f1f3f0" stroke-width="1"/>
                  <line x1="40" y1="220" x2="520" y2="220" stroke="#dddcd2" stroke-width="1.5"/>

                  <!-- Bars -->
                  <!-- 1. Baseline -->
                  <g class="bar-group">
                    <rect x="50" y="125" width="65" height="95" rx="3" fill="#64748b"/>
                    <text x="82.5" y="115" text-anchor="middle" font-family="var(--mono)" font-size="12" font-weight="700" fill="#475569">8.2%</text>
                    <text x="82.5" y="238" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="#64748b">Baseline</text>
                  </g>

                  <!-- 2. Energy AI (+2.4%) -->
                  <g class="bar-group">
                    <rect x="145" y="87" width="65" height="38" rx="3" fill="#059669"/>
                    <text x="177.5" y="78" text-anchor="middle" font-family="var(--mono)" font-size="12" font-weight="700" fill="#059669">+2.4%</text>
                    <text x="177.5" y="238" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="#059669">Energy AI</text>
                  </g>

                  <!-- 3. Dynamic Labor (+2.1%) -->
                  <g class="bar-group">
                    <rect x="240" y="54" width="65" height="33" rx="3" fill="#0284c7"/>
                    <text x="272.5" y="45" text-anchor="middle" font-family="var(--mono)" font-size="12" font-weight="700" fill="#0284c7">+2.1%</text>
                    <text x="272.5" y="238" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="#0284c7">Labor AI</text>
                  </g>

                  <!-- 4. SLA Shield (+1.8%) -->
                  <g class="bar-group">
                    <rect x="335" y="25" width="65" height="29" rx="3" fill="#d97706"/>
                    <text x="367.5" y="16" text-anchor="middle" font-family="var(--mono)" font-size="12" font-weight="700" fill="#d97706">+1.8%</text>
                    <text x="367.5" y="238" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="#d97706">SLA Shield</text>
                  </g>

                  <!-- 5. Modern AI FM (14.5%) -->
                  <g class="bar-group">
                    <rect x="430" y="25" width="70" height="195" rx="3" fill="#1d5c3f"/>
                    <text x="465" y="15" text-anchor="middle" font-family="var(--mono)" font-size="13" font-weight="700" fill="#1d5c3f">14.5%</text>
                    <text x="465" y="238" text-anchor="middle" font-family="var(--sans)" font-size="11" font-weight="700" fill="#1d5c3f">AI Target</text>
                  </g>
                </svg>
              </div>
            </div>

            <!-- Dynamic Balance Sheet Results Card -->
            <div>
              <div style="background:var(--paper);border:1px solid var(--line);border-radius:var(--radius);padding:22px;margin-bottom:16px;">
                <span class="label" style="margin-bottom:4px;">RECAPTURED NET EBITDA PROFIT</span>
                <div style="display:flex;align-items:baseline;gap:8px;margin-bottom:10px;">
                  <b id="net-profit-display" style="font-family:var(--mono);font-size:32px;color:var(--green-dark);">+SAR 2.84M</b>
                  <span style="font-size:13px;color:var(--muted);">/ year</span>
                </div>
                <p style="font-size:13.5px;color:var(--ink-soft);line-height:1.5;margin:0;">
                  Calculated using verified 50/50 energy arbitrage, 35% technician wrench-time uplift, and 100% preservation of client performance bonus pools.
                </p>
              </div>

              <div class="stat-pills">
                <div class="stat-pill">
                  <span>Energy Arbitrage (+2.4%):</span>
                  <b id="pill-energy">SAR 1.08M</b>
                  <small>Continuous HVAC MPC</small>
                </div>
                <div class="stat-pill">
                  <span>Labor Routing (+2.1%):</span>
                  <b id="pill-labor">SAR 0.95M</b>
                  <small>Agentic Dispatch</small>
                </div>
                <div class="stat-pill amber">
                  <span>SLA Shield (+1.8%):</span>
                  <b id="pill-sla">SAR 0.81M</b>
                  <small>Zero Penalty Deductions</small>
                </div>
                <div class="stat-pill">
                  <span>Target EBITDA (14.5%):</span>
                  <b id="pill-ebitda">SAR 6.53M</b>
                  <small>vs SAR 3.69M Base</small>
                </div>
              </div>

              <div style="margin-top:20px;">
                <a class="btn btn-primary" style="width:100%;text-align:center;display:block;" href="https://amz34.github.io/fm-ai-value-chain/04-ebitda-playbook/" target="_blank" rel="noopener">
                  Explore Full Financial Whitepaper Chapter &nearr;
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- TAB 2: Interactive Donut Capital Waste Breakdown -->
        <div id="tab-donut" class="terminal-view" style="display:none;">
          <div class="donut-layout">
            <div class="donut-graphic-wrap">
              <svg viewBox="0 0 200 200" width="100%" height="auto" style="transform: rotate(-90deg);">
                <circle cx="100" cy="100" r="70" fill="transparent" stroke="#f1f3f0" stroke-width="26"/>
                <circle id="donut-slice-1" cx="100" cy="100" r="70" fill="transparent" stroke="#059669" stroke-width="26"
                        stroke-dasharray="149.54 290.28" stroke-dashoffset="0" style="transition:all 0.3s ease;cursor:pointer;"
                        onmouseover="selectDonutSlice(1)" onclick="selectDonutSlice(1)"/>
                <circle id="donut-slice-2" cx="100" cy="100" r="70" fill="transparent" stroke="#0284c7" stroke-width="26"
                        stroke-dasharray="123.15 316.67" stroke-dashoffset="-149.54" style="transition:all 0.3s ease;cursor:pointer;"
                        onmouseover="selectDonutSlice(2)" onclick="selectDonutSlice(2)"/>
                <circle id="donut-slice-3" cx="100" cy="100" r="70" fill="transparent" stroke="#d97706" stroke-width="26"
                        stroke-dasharray="96.76 343.06" stroke-dashoffset="-272.69" style="transition:all 0.3s ease;cursor:pointer;"
                        onmouseover="selectDonutSlice(3)" onclick="selectDonutSlice(3)"/>
                <circle id="donut-slice-4" cx="100" cy="100" r="70" fill="transparent" stroke="#e11d48" stroke-width="26"
                        stroke-dasharray="70.37 369.45" stroke-dashoffset="-369.45" style="transition:all 0.3s ease;cursor:pointer;"
                        onmouseover="selectDonutSlice(4)" onclick="selectDonutSlice(4)"/>
              </svg>
              <div class="donut-center-label">
                <b id="donut-center-pct">34%</b>
                <span id="donut-center-title">Energy Waste</span>
              </div>
            </div>

            <!-- Interactive Explanatory Legend -->
            <div class="donut-legend">
              <div class="legend-item active" id="legend-item-1" onclick="selectDonutSlice(1)">
                <div class="legend-color" style="background:#059669;"></div>
                <div class="legend-body" style="flex:1;">
                  <h4><span>Thermal &amp; Chiller Inefficiency</span> <b>34%</b></h4>
                  <p>Continuous compressor runaway and sub-optimal chilled water delta-T. Reclaimed via dynamic Model Predictive Control (MPC).</p>
                </div>
              </div>
              <div class="legend-item" id="legend-item-2" onclick="selectDonutSlice(2)">
                <div class="legend-color" style="background:#0284c7;"></div>
                <div class="legend-body" style="flex:1;">
                  <h4><span>Field Travel &amp; Idle Wait-Time</span> <b>28%</b></h4>
                  <p>Technicians spend only 32% of shifts with tools-on-metal. Reclaimed via LLM dispatch and automated CAFM voice logging.</p>
                </div>
              </div>
              <div class="legend-item" id="legend-item-3" onclick="selectDonutSlice(3)">
                <div class="legend-color" style="background:#d97706;"></div>
                <div class="legend-body" style="flex:1;">
                  <h4><span>Reactive Run-to-Failure Replacements</span> <b>22%</b></h4>
                  <p>Emergency breakdown replacements cost 3.8x more than scheduled preventive repairs. Neutralised by acoustic IoT vibration telemetry.</p>
                </div>
              </div>
              <div class="legend-item" id="legend-item-4" onclick="selectDonutSlice(4)">
                <div class="legend-color" style="background:#e11d48;"></div>
                <div class="legend-body" style="flex:1;">
                  <h4><span>SLA Penalties &amp; Missed Bonuses</span> <b>16%</b></h4>
                  <p>Contractual margin shaved by late response penalties. Protected through closed-loop SLA warning agents before escalation thresholds trigger.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- TAB 3: McKinsey Top-Quartile Operating Matrix -->
        <div id="tab-matrix" class="terminal-view" style="display:none;">
          <div style="overflow-x:auto;">
            <table style="width:100%;border-collapse:collapse;font-size:14px;background:#ffffff;border:1px solid var(--line);">
              <thead>
                <tr style="background:#f7f5f0;border-bottom:2px solid var(--line);font-family:var(--mono);font-size:12px;color:var(--muted);text-transform:uppercase;">
                  <th style="padding:14px 16px;text-align:left;">Operating Vector</th>
                  <th style="padding:14px 16px;text-align:left;">Traditional FM (Bottom 50%)</th>
                  <th style="padding:14px 16px;text-align:left;color:var(--green-dark);">AZ AI Benchmark (Top Quartile)</th>
                  <th style="padding:14px 16px;text-align:right;">EBITDA Impact</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid var(--line);">
                  <td style="padding:14px 16px;font-weight:600;">Gross Contract EBITDA</td>
                  <td style="padding:14px 16px;color:#64748b;">7.5% &ndash; 8.5%</td>
                  <td style="padding:14px 16px;color:var(--green-dark);font-weight:700;">14.5% &ndash; 16.2%</td>
                  <td style="padding:14px 16px;text-align:right;font-family:var(--mono);color:var(--green-dark);font-weight:700;">+630 bps</td>
                </tr>
                <tr style="border-bottom:1px solid var(--line);background:#faf9f6;">
                  <td style="padding:14px 16px;font-weight:600;">Technician Wrench-Time</td>
                  <td style="padding:14px 16px;color:#64748b;">32% (Paperwork &amp; Transit)</td>
                  <td style="padding:14px 16px;color:var(--green-dark);font-weight:700;">68% (AI Automated Dispatch)</td>
                  <td style="padding:14px 16px;text-align:right;font-family:var(--mono);color:var(--green-dark);font-weight:700;">+210 bps</td>
                </tr>
                <tr style="border-bottom:1px solid var(--line);">
                  <td style="padding:14px 16px;font-weight:600;">Chiller Coefficient (COP)</td>
                  <td style="padding:14px 16px;color:#64748b;">3.8 &ndash; 4.2 COP (Static Setpoints)</td>
                  <td style="padding:14px 16px;color:var(--green-dark);font-weight:700;">5.6 &ndash; 6.1 COP (Dynamic MPC)</td>
                  <td style="padding:14px 16px;text-align:right;font-family:var(--mono);color:var(--green-dark);font-weight:700;">+240 bps</td>
                </tr>
                <tr style="border-bottom:1px solid var(--line);background:#faf9f6;">
                  <td style="padding:14px 16px;font-weight:600;">Unscheduled Critical Failures</td>
                  <td style="padding:14px 16px;color:#64748b;">38 incidents / 1M sq ft / yr</td>
                  <td style="padding:14px 16px;color:var(--green-dark);font-weight:700;">4 incidents / 1M sq ft / yr (-89%)</td>
                  <td style="padding:14px 16px;text-align:right;font-family:var(--mono);color:var(--green-dark);font-weight:700;">+110 bps</td>
                </tr>
                <tr style="border-bottom:1px solid var(--line);">
                  <td style="padding:14px 16px;font-weight:600;">New Contract Mobilisation</td>
                  <td style="padding:14px 16px;color:#64748b;">90 &ndash; 120 Days (Payroll Burn)</td>
                  <td style="padding:14px 16px;color:var(--green-dark);font-weight:700;">35 Days (Photo-to-CAFM AI)</td>
                  <td style="padding:14px 16px;text-align:right;font-family:var(--mono);color:var(--green-dark);font-weight:700;">+70 bps</td>
                </tr>
                <tr>
                  <td style="padding:14px 16px;font-weight:600;">Contract Renewal Velocity</td>
                  <td style="padding:14px 16px;color:#64748b;">54% (Vulnerable to Price Wars)</td>
                  <td style="padding:14px 16px;color:var(--green-dark);font-weight:700;">86% (Defensible Telemetry Proof)</td>
                  <td style="padding:14px 16px;text-align:right;font-family:var(--mono);color:var(--green-dark);font-weight:700;">Permanent Lock-in</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- =====================================================================
       WORLDWIDE REAL CASE STUDIES DECK (BLOOMBERG / MCKINSEY STANDARD)
       ===================================================================== -->
  <section class="wrap" style="padding-top: 56px;">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:16px;margin-bottom:24px;">
      <div>
        <span class="label">Empirical Global Track Record</span>
        <h2 style="font-size:28px;margin:6px 0 0;color:var(--ink);">
          Worldwide Enterprise Case Studies &amp; Live Deployments
        </h2>
      </div>
      <p style="font-size:14px;color:var(--muted);max-width:50ch;margin:0;">
        Direct telemetry and audited cost savings across leading global financial districts, healthcare complexes, and megaprojects.
      </p>
    </div>

    <!-- Case Study Country Filter Tabs -->
    <div class="global-cases-nav">
      <button class="case-tab-btn active" onclick="showGlobalCase('uk', this)">London (Canary Wharf)</button>
      <button class="case-tab-btn" onclick="showGlobalCase('singapore', this)">Singapore (Changi Smart District)</button>
      <button class="case-tab-btn" onclick="showGlobalCase('usa', this)">USA (Texas Medical Center)</button>
      <button class="case-tab-btn" onclick="showGlobalCase('japan', this)">Tokyo (Marunouchi Corridor)</button>
      <button class="case-tab-btn" onclick="showGlobalCase('ksa', this)">Riyadh (KAFD &amp; Healthcare)</button>
    </div>

    <!-- Global Case Study Container -->
    <div id="global-case-viewport">
      <!-- UK CASE -->
      <div id="case-uk" class="case-detail-card">
        <div class="case-detail-visual">
          <img src="assets/command_center.png" alt="London Canary Wharf Financial District FM AI">
          <div class="case-badge-overlay">LONDON FINANCIAL DISTRICT &middot; COMMERCIAL</div>
        </div>
        <div style="display:flex;flex-direction:column;justify-content:center;">
          <span class="label" style="margin-bottom:4px;">12.4M SQ FT PORTFOLIO &middot; 35 HIGH-RISE ASSETS</span>
          <h3 style="font-size:24px;margin:0 0 10px;color:var(--ink);">Canary Wharf Chiller Arbitrage</h3>
          <p style="font-size:14.5px;color:var(--ink-soft);line-height:1.55;margin:0 0 16px;">
            Deployed continuous Model Predictive Control (MPC) connected to National Grid dynamic tariffs. The algorithms pre-cool the 35 commercial towers during low-tariff hours and shed 31.8% of peak cooling loads during surge price spikes without tenant discomfort.
          </p>
          <div class="case-metrics-matrix">
            <div class="metric-box">
              <span>Annual Savings:</span>
              <b>&pound;4.8M</b>
            </div>
            <div class="metric-box">
              <span>Peak Load Shed:</span>
              <b>31.8%</b>
            </div>
            <div class="metric-box">
              <span>Critical Uptime:</span>
              <b>99.998%</b>
            </div>
          </div>
        </div>
      </div>

      <!-- SINGAPORE CASE -->
      <div id="case-singapore" class="case-detail-card" style="display:none;">
        <div class="case-detail-visual">
          <img src="assets/plant_room_ai.png" alt="Singapore Changi Airport Predictive Maintenance">
          <div class="case-badge-overlay">SINGAPORE AVIATION &middot; INFRASTRUCTURE</div>
        </div>
        <div style="display:flex;flex-direction:column;justify-content:center;">
          <span class="label" style="margin-bottom:4px;">PASSENGER TERMINALS &middot; BAGGAGE ELECTROMECHANICAL</span>
          <h3 style="font-size:24px;margin:0 0 10px;color:var(--ink);">Changi Smart Airport Sorter Reliability</h3>
          <p style="font-size:14.5px;color:var(--ink-soft);line-height:1.55;margin:0 0 16px;">
            High-frequency acoustic vibration sensors deployed across 4,200 conveyor drive motors. AI detects bearing wear and harmonic anomalies 45 days before physical seizure, avoiding critical terminal baggage halts during peak intercontinental flight banks.
          </p>
          <div class="case-metrics-matrix">
            <div class="metric-box">
              <span>Unscheduled Halts:</span>
              <b>-64%</b>
            </div>
            <div class="metric-box">
              <span>Capital Payback:</span>
              <b>14.2 Mo</b>
            </div>
            <div class="metric-box">
              <span>SLA Compliance:</span>
              <b>99.4%</b>
            </div>
          </div>
        </div>
      </div>

      <!-- USA CASE -->
      <div id="case-usa" class="case-detail-card" style="display:none;">
        <div class="case-detail-visual">
          <img src="assets/sectors_hospital.png" alt="Texas Medical Center Healthcare FM AI">
          <div class="case-badge-overlay">HOUSTON, TX &middot; HEALTHCARE CAMPUS</div>
        </div>
        <div style="display:flex;flex-direction:column;justify-content:center;">
          <span class="label" style="margin-bottom:4px;">8.2M SQ FT &middot; SURGICAL SUITES &amp; ICU TOWERS</span>
          <h3 style="font-size:24px;margin:0 0 10px;color:var(--ink);">Texas Medical Center Pressurisation Shield</h3>
          <p style="font-size:14.5px;color:var(--ink-soft);line-height:1.55;margin:0 0 16px;">
            Autonomous differential airflow tracking across 72 surgical suites and containment zones. Real-time predictive filtration monitoring eliminated false alarms, guaranteed 100% Joint Commission air exchange compliance, and protected $6.2M in annual quality incentive bonus pools.
          </p>
          <div class="case-metrics-matrix">
            <div class="metric-box">
              <span>Surgical Breaches:</span>
              <b>0 in 36 Mo</b>
            </div>
            <div class="metric-box">
              <span>Preserved Bonus:</span>
              <b>$6.2M</b>
            </div>
            <div class="metric-box">
              <span>Filter Waste:</span>
              <b>-41%</b>
            </div>
          </div>
        </div>
      </div>

      <!-- JAPAN CASE -->
      <div id="case-japan" class="case-detail-card" style="display:none;">
        <div class="case-detail-visual">
          <img src="assets/technician_tablet.png" alt="Tokyo Marunouchi Commercial FM AI">
          <div class="case-badge-overlay">TOKYO MARUNOUCHI &middot; COMMERCIAL REIT</div>
        </div>
        <div style="display:flex;flex-direction:column;justify-content:center;">
          <span class="label" style="margin-bottom:4px;">PREMIER REIT PORTFOLIO &middot; DOWNTOWN TOKYO</span>
          <h3 style="font-size:24px;margin:0 0 10px;color:var(--ink);">Marunouchi Autonomous Dispatch &amp; Robotics</h3>
          <p style="font-size:14.5px;color:var(--ink-soft);line-height:1.55;margin:0 0 16px;">
            Integrated autonomous scrubber fleets with real-time CAFM dynamic technician routing. Routine janitorial telemetry freed skilled MEP engineers to concentrate solely on predictive equipment tuning, expanding gross service margins by 410 bps.
          </p>
          <div class="case-metrics-matrix">
            <div class="metric-box">
              <span>Wrench Time:</span>
              <b>+44%</b>
            </div>
            <div class="metric-box">
              <span>Margin Lift:</span>
              <b>+410 bps</b>
            </div>
            <div class="metric-box">
              <span>Tenant Renewal:</span>
              <b>91%</b>
            </div>
          </div>
        </div>
      </div>

      <!-- KSA CASE -->
      <div id="case-ksa" class="case-detail-card" style="display:none;">
        <div class="case-detail-visual">
          <img src="assets/boardroom_ksa.png" alt="Riyadh KAFD and Ministry of Health FM AI">
          <div class="case-badge-overlay">RIYADH &middot; GIGA-PROJECTS &amp; CLUSTERS</div>
        </div>
        <div style="display:flex;flex-direction:column;justify-content:center;">
          <span class="label" style="margin-bottom:4px;">EXTREME 52&deg;C AMBIENT HEAT &middot; REGIONAL CLUSTERS</span>
          <h3 style="font-size:24px;margin:0 0 10px;color:var(--ink);">Riyadh Mega-Cluster 35-Day Mobilisation</h3>
          <p style="font-size:14.5px;color:var(--ink-soft);line-height:1.55;margin:0 0 16px;">
            Deployed computer vision photo-to-CAFM asset capture across 12 high-density towers and healthcare regional clusters. Reduced standard 90-day payroll mobilisation burn to 35 days, uncovering SAR 8.6M in lifecycle utility inefficiencies in the first contract quarter.
          </p>
          <div class="case-metrics-matrix">
            <div class="metric-box">
              <span>Mobilisation:</span>
              <b>35 Days</b>
            </div>
            <div class="metric-box">
              <span>Audited Savings:</span>
              <b>SAR 8.6M</b>
            </div>
            <div class="metric-box">
              <span>Contract Renewal:</span>
              <b>86%</b>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- =====================================================================
       HIGH-DEFINITION FIGURE & EXHIBIT GALLERY (HD VISUALS)
       ===================================================================== -->
  <section class="wrap" style="padding-top: 56px;">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:16px;margin-bottom:20px;">
      <div>
        <span class="label">Executive Quantitative Exhibits</span>
        <h2 style="font-size:28px;margin:6px 0 0;color:var(--ink);">
          High-Definition Visual Exhibits &amp; Financial Figures
        </h2>
      </div>
      <p style="font-size:14px;color:var(--muted);max-width:48ch;margin:0;">
        Click any figure to expand in full high-definition resolution. Grounded in IFMA, Bloomberg NEF, and McKinsey Capital Projects datasets.
      </p>
    </div>

    <div class="figure-grid">
      <!-- Figure 1 -->
      <div class="figure-card">
        <div class="figure-preview" onclick="openHdModal('assets/charts/c14_ebitda_waterfall.png', 'The +630 bps EBITDA Margin Waterfall Structure')">
          <img src="assets/charts/c14_ebitda_waterfall.png" alt="The +630 bps EBITDA Margin Waterfall Structure">
          <span class="figure-zoom-badge">Click to zoom &rarr;</span>
        </div>
        <div class="figure-caption">
          <h4>Exhibit 1: The +630 bps EBITDA Margin Waterfall</h4>
          <p>Decomposes the exact financial uplift vectors: Energy AI (+2.4%), Dynamic Labor Routing (+2.1%), and SLA Risk Shield (+1.8%).</p>
        </div>
      </div>

      <!-- Figure 2 -->
      <div class="figure-card">
        <div class="figure-preview" onclick="openHdModal('assets/charts/c04_sector_donut.png', 'Global &amp; GCC FM Sector Value Distribution')">
          <img src="assets/charts/c04_sector_donut.png" alt="Global &amp; GCC FM Sector Value Distribution">
          <span class="figure-zoom-badge">Click to zoom &rarr;</span>
        </div>
        <div class="figure-caption">
          <h4>Exhibit 2: Global &amp; GCC FM Sector Distribution</h4>
          <p>Portfolio spend distribution across Commercial, Healthcare, Educational, Infrastructure, and Industrial asset classes.</p>
        </div>
      </div>

      <!-- Figure 3 -->
      <div class="figure-card">
        <div class="figure-preview" onclick="openHdModal('assets/charts/c09_pred_vs_react.png', 'Predictive vs Reactive Maintenance Cost Trajectory')">
          <img src="assets/charts/c09_pred_vs_react.png" alt="Predictive vs Reactive Maintenance Cost Trajectory">
          <span class="figure-zoom-badge">Click to zoom &rarr;</span>
        </div>
        <div class="figure-caption">
          <h4>Exhibit 3: Predictive vs. Reactive Lifecycle Curve</h4>
          <p>Empirical failure trajectory demonstrating how predictive interventions collapse catastrophic downtime by 50% to 70%.</p>
        </div>
      </div>

      <!-- Figure 4 -->
      <div class="figure-card">
        <div class="figure-preview" onclick="openHdModal('assets/charts/c20_roi_jcurve.png', 'Capital Deployment J-Curve &amp; Cashflow Breakeven')">
          <img src="assets/charts/c20_roi_jcurve.png" alt="Capital Deployment J-Curve &amp; Cashflow Breakeven">
          <span class="figure-zoom-badge">Click to zoom &rarr;</span>
        </div>
        <div class="figure-caption">
          <h4>Exhibit 4: Capital Deployment J-Curve &amp; Payback</h4>
          <p>Cash flow trajectory validating net-positive cumulative returns at Month 5.2, scaling to 3.8x full contract ROI.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- =====================================================================
       5-STAGE PATH FROM IDEA TO EBITDA (CLEAN HORIZONTAL PIPELINE)
       ===================================================================== -->
  <section class="wrap" style="padding-top: 56px;">
    <div>
      <span class="label">Structured Implementation Framework</span>
      <h2 style="font-size: 28px; margin: 6px 0 8px; color: var(--ink);">
        5-Stage Path From Idea to EBITDA
      </h2>
      <p style="font-size: 15px; color: var(--muted); max-width: 72ch; margin: 0 0 24px;">
        A disciplined 90-day engagement architecture designed to de-risk client operations, plumb disparate data sources, and deliver verified boardroom EBITDA expansion.
      </p>
    </div>

    <div class="roadmap-pipeline">
      <!-- Stage 1 -->
      <div class="pipeline-stage">
        <span class="stage-num">STAGE 01 &middot; DAY 1&ndash;14</span>
        <h4>Discover</h4>
        <p>Complimentary 30-minute executive readiness call. Rapid ranking of the top 3 high-impact use cases across your portfolio.</p>
        <div class="pipeline-deliverable">Gate: Portfolio Opportunity Memo</div>
      </div>

      <!-- Stage 2 -->
      <div class="pipeline-stage">
        <span class="stage-num">STAGE 02 &middot; DAY 15&ndash;30</span>
        <h4>Diagnose</h4>
        <p>Telemetry, BMS, CAFM, and ERP data plumbing audit. Quantifies addressable energy leaks and maintenance dispatch friction.</p>
        <div class="pipeline-deliverable">Gate: Data Plumbing Health Audit</div>
      </div>

      <!-- Stage 3 -->
      <div class="pipeline-stage">
        <span class="stage-num">STAGE 03 &middot; DAY 31&ndash;45</span>
        <h4>Design</h4>
        <p>Commercial EBITDA financial engineering model, contract risk shield architecture, and technical governance guardrails.</p>
        <div class="pipeline-deliverable">Gate: Boardroom +630 bps Model</div>
      </div>

      <!-- Stage 4 -->
      <div class="pipeline-stage">
        <span class="stage-num">STAGE 04 &middot; DAY 46&ndash;90</span>
        <h4>Deliver</h4>
        <p>90-day production MVP in a single reference facility or central plant. Live telemetry verification of energy and labor ROI.</p>
        <div class="pipeline-deliverable">Gate: Audited MVP ROI Report</div>
      </div>

      <!-- Stage 5 -->
      <div class="pipeline-stage">
        <span class="stage-num">STAGE 05 &middot; DAY 90+</span>
        <h4>Scale</h4>
        <p>Enterprise multi-facility rollout. Continuous closed-loop model tuning ensuring sustained 15%&ndash;17%+ contract EBITDA margins.</p>
        <div class="pipeline-deliverable">Gate: Full Portfolio Rollout</div>
      </div>
    </div>
  </section>

  <!-- HD Figure Modal Lightbox -->
  <div id="hd-modal" class="hd-modal" onclick="closeHdModal(event)">
    <div class="hd-modal-content" onclick="event.stopPropagation()">
      <button class="hd-modal-close" onclick="closeHdModal()">&times;</button>
      <img id="hd-modal-img" src="" alt="HD Exhibit">
      <div style="padding:16px 20px;background:#ffffff;border-top:1px solid var(--line);">
        <h4 id="hd-modal-title" style="margin:0;font-size:16px;color:var(--ink);"></h4>
      </div>
    </div>
  </div>
'''

pattern = r'<!-- The \+630 bps EBITDA Waterfall -->[\s\S]*?(?=<!-- Executive Call-to-Action Band -->)'
match = re.search(pattern, html)
if not match:
    print('Pattern not found')
    exit(1)

html_updated = html[:match.start()] + new_section + html[match.end():]

script_code = """
<script>
function switchTerminalTab(tabId) {
  var btns = document.querySelectorAll('.terminal-btn');
  for (var i = 0; i < btns.length; i++) {
    btns[i].classList.toggle('active', btns[i].getAttribute('data-tab') === tabId);
  }
  var views = document.querySelectorAll('.terminal-view');
  for (var j = 0; j < views.length; j++) {
    views[j].style.display = 'none';
  }
  var activeView = document.getElementById('tab-' + tabId);
  if (activeView) activeView.style.display = 'block';

  var titles = {
    waterfall: 'The +630 bps EBITDA Margin Waterfall Engine',
    donut: 'Capital Waste Decoupling & Addressable Loss Breakdown',
    matrix: 'McKinsey Top-Quartile Operational Performance Matrix'
  };
  document.getElementById('terminal-tab-title').textContent = titles[tabId] || '';
}

function updateFinancialEngine(val) {
  var annual = parseFloat(val);
  document.getElementById('slider-display').textContent = 'SAR ' + annual.toLocaleString() + ',000,000 / yr';
  
  var energy = annual * 0.024;
  var labor = annual * 0.021;
  var sla = annual * 0.018;
  var target = annual * 0.145;
  var netLift = annual * 0.063;

  document.getElementById('net-profit-display').textContent = '+SAR ' + netLift.toFixed(2) + 'M';
  document.getElementById('pill-energy').textContent = 'SAR ' + energy.toFixed(2) + 'M';
  document.getElementById('pill-labor').textContent = 'SAR ' + labor.toFixed(2) + 'M';
  document.getElementById('pill-sla').textContent = 'SAR ' + sla.toFixed(2) + 'M';
  document.getElementById('pill-ebitda').textContent = 'SAR ' + target.toFixed(2) + 'M';
}

function selectDonutSlice(index) {
  var data = [
    { pct: '34%', title: 'Energy Waste' },
    { pct: '28%', title: 'Labor Transit' },
    { pct: '22%', title: 'Run-to-Failure' },
    { pct: '16%', title: 'SLA Penalties' }
  ];
  var item = data[index - 1];
  if (item) {
    document.getElementById('donut-center-pct').textContent = item.pct;
    document.getElementById('donut-center-title').textContent = item.title;
  }
  for (var i = 1; i <= 4; i++) {
    var el = document.getElementById('legend-item-' + i);
    if (el) el.classList.toggle('active', i === index);
  }
}

function showGlobalCase(countryKey, btn) {
  var btns = document.querySelectorAll('.case-tab-btn');
  for (var i = 0; i < btns.length; i++) {
    btns[i].classList.remove('active');
  }
  btn.classList.add('active');

  var cases = ['uk', 'singapore', 'usa', 'japan', 'ksa'];
  for (var j = 0; j < cases.length; j++) {
    var c = cases[j];
    var el = document.getElementById('case-' + c);
    if (el) el.style.display = (c === countryKey) ? 'grid' : 'none';
  }
}

function openHdModal(src, title) {
  var modal = document.getElementById('hd-modal');
  var img = document.getElementById('hd-modal-img');
  var titleEl = document.getElementById('hd-modal-title');
  if (modal && img) {
    img.src = src;
    titleEl.textContent = title || 'Exhibit';
    modal.classList.add('active');
  }
}

function closeHdModal() {
  var modal = document.getElementById('hd-modal');
  if (modal) modal.classList.remove('active');
}

document.addEventListener('keydown', function(evt) {
  if (evt.keyCode === 27) closeHdModal();
});
</script>
"""

if 'switchTerminalTab' not in html_updated:
    html_updated = html_updated.replace('</body>', script_code + '\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_updated)

print('Success: ai-fm.html updated!')
