# AZ Consultants KSA — Official Production Website

Official static website & lead intake gateway for **AZ Consultants** (Riyadh, Kingdom of Saudi Arabia).

## Features
- **Interactive Mandate Scoping Questionnaire**: Extra-Large typography, 10-step Typeform UX, dynamic name interpolation.
- **Embedded In-Page Forms**: Embedded directly in the Enquiry panel of `contact.html` and the homepage `#enquiry` section.
- **Automated Telegram Lead Dispatch**: Serverless Cloudflare Pages Function (`functions/api/inquiry.js`) delivering instant lead dossiers to `@AzGem_Bot` (`chat_id: 8843884232`).
- **Dynamic Viability Scorecard**: Instant 90%+ viability rating, 30% LCGPA mandate analysis, official verification seal, and 1-click printable PDF dossier.

## Cloudflare Pages Deployment Configuration
- **Framework preset**: `None`
- **Build command**: *(None / leave empty)*
- **Build output directory**: `/` *(root)*
- **Root directory**: `/` *(root)*
- **Functions directory**: `functions/` *(automatically detected by Cloudflare Pages)*
