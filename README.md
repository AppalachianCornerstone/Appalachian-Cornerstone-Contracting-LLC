# Appalachian-Cornerstone-Contracting-LLC
Website for Appalachian Cornerstone Contracting, LLC
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Appalachian Cornerstone Contracting, LLC — General contracting services in Morehead, Kentucky.">
  <title>Appalachian Cornerstone Contracting, LLC</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="topbar">
    <div class="container nav">
      <a class="brand" href="#home">
        <span class="mark">AC</span>
        <span>Appalachian Cornerstone<br><small>Contracting, LLC</small></span>
      </a>
      <a class="nav-call" href="tel:16065488297">Call 606-548-8297</a>
    </div>
  </header>

  <main>
    <section id="home" class="hero">
      <div class="container hero-content">
        <p class="eyebrow">GENERAL CONTRACTING • MOREHEAD, KENTUCKY</p>
        <h1>Built on hard work.<br><span>Backed by craftsmanship.</span></h1>
        <p class="lead">Appalachian Cornerstone Contracting, LLC provides dependable general contracting services for homeowners and property owners in Morehead and the surrounding area.</p>
        <div class="actions">
          <a class="btn primary" href="tel:16065488297">Call for a Quote</a>
          <a class="btn secondary" href="mailto:AppalachianCornerstoneContract@gmail.com?subject=Project%20Quote%20Request">Request a Quote by Email</a>
        </div>
      </div>
    </section>

    <section class="trust">
      <div class="container trust-grid">
        <div><strong>Local</strong><span>Morehead, Kentucky</span></div>
        <div><strong>Professional</strong><span>General Contracting</span></div>
        <div><strong>Reliable</strong><span>Quality-focused service</span></div>
      </div>
    </section>

    <section id="services" class="section">
      <div class="container">
        <p class="eyebrow">WHAT WE DO</p>
        <h2>General Contracting Services</h2>
        <p class="section-intro">Whether you're planning an improvement, repair, renovation, or larger project, Appalachian Cornerstone Contracting is ready to discuss your needs.</p>
        <div class="cards">
          <article class="card">
            <div class="icon">01</div>
            <h3>General Contracting</h3>
            <p>Coordinated construction and improvement work with attention to planning, communication, and workmanship.</p>
          </article>
          <article class="card">
            <div class="icon">02</div>
            <h3>Renovations & Improvements</h3>
            <p>Practical upgrades and renovation projects designed around your property, priorities, and budget.</p>
          </article>
          <article class="card">
            <div class="icon">03</div>
            <h3>Repairs & Projects</h3>
            <p>Help with property repairs and construction projects that need dependable hands and careful execution.</p>
          </article>
        </div>
      </div>
    </section>

    <section id="about" class="section dark">
      <div class="container about-grid">
        <div>
          <p class="eyebrow">ABOUT THE COMPANY</p>
          <h2>Your project starts with a solid cornerstone.</h2>
        </div>
        <div>
          <p>Appalachian Cornerstone Contracting, LLC is a Morehead, Kentucky general contracting company focused on dependable service and quality workmanship.</p>
          <p>Our goal is simple: communicate clearly, do the work right, and treat every project and property with respect.</p>
          <a class="text-link" href="mailto:AppalachianCornerstoneContract@gmail.com?subject=Project%20Inquiry">Start a conversation →</a>
        </div>
      </div>
    </section>

    <section id="contact" class="section contact">
      <div class="container contact-grid">
        <div>
          <p class="eyebrow">GET IN TOUCH</p>
          <h2>Let's talk about your project.</h2>
          <p>Tell us what you're planning and we'll be happy to discuss the next step.</p>
        </div>
        <div class="contact-box">
          <a href="tel:16065488297"><span>PHONE</span>606-548-8297</a>
          <a href="mailto:AppalachianCornerstoneContract@gmail.com"><span>EMAIL</span>AppalachianCornerstoneContract@gmail.com</a>
          <div><span>LOCATION</span>Morehead, Kentucky</div>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container footer">
      <p>© 2026 Appalachian Cornerstone Contracting, LLC. All rights reserved.</p>
      <p>Morehead, Kentucky</p>
    </div>
  </footer>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Oswald:wght@500;600&display=swap');

:root{
  --ink:#171a19; --muted:#68706d; --paper:#f5f3ee; --white:#fff;
  --accent:#b66a2b; --accent-dark:#8e4e1d; --line:#ddd9d0;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:"DM Sans",Arial,sans-serif;line-height:1.6}
.container{width:min(1120px,calc(100% - 40px));margin:auto}
.topbar{background:#121514;color:#fff;border-bottom:1px solid #2b302e}
.nav{height:78px;display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:12px;color:#fff;text-decoration:none;font-weight:700;line-height:1.05}
.brand small{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:#c6cbc8}
.mark{width:40px;height:40px;border:2px solid var(--accent);display:grid;place-items:center;font-family:Oswald,sans-serif;color:#fff}
.nav-call{color:#fff;text-decoration:none;font-weight:700;border-bottom:1px solid var(--accent);padding-bottom:3px}
.hero{min-height:650px;display:flex;align-items:center;background:
linear-gradient(90deg,rgba(12,15,14,.96) 0%,rgba(12,15,14,.82) 52%,rgba(12,15,14,.42) 100%),
linear-gradient(135deg,#242927,#555a56);color:#fff}
.hero-content{padding:90px 0;max-width:780px}
.eyebrow{font-size:.78rem;letter-spacing:.18em;font-weight:700;color:var(--accent);margin:0 0 16px}
h1,h2{font-family:Oswald,Impact,sans-serif;text-transform:uppercase;line-height:1.02;letter-spacing:.015em;margin:0}
h1{font-size:clamp(3rem,7vw,6rem)}
h1 span{color:#d98a4c}
.lead{font-size:1.15rem;max-width:700px;color:#e2e5e2;margin:26px 0 34px}
.actions{display:flex;flex-wrap:wrap;gap:12px}
.btn{display:inline-block;text-decoration:none;font-weight:700;padding:13px 20px;border:1px solid transparent}
.primary{background:var(--accent);color:#fff}.primary:hover{background:var(--accent-dark)}
.secondary{border-color:#8d938f;color:#fff}.secondary:hover{border-color:#fff}
.trust{background:#fff;border-bottom:1px solid var(--line)}
.trust-grid{display:grid;grid-template-columns:repeat(3,1fr)}
.trust-grid div{padding:25px 20px;border-right:1px solid var(--line)}
.trust-grid div:last-child{border:0}
.trust strong,.trust span{display:block}.trust strong{font-family:Oswald,sans-serif;text-transform:uppercase;font-size:1.2rem}.trust span{color:var(--muted);font-size:.9rem}
.section{padding:100px 0}.section h2{font-size:clamp(2.3rem,5vw,4rem);max-width:760px}
.section-intro{max-width:700px;color:var(--muted);font-size:1.05rem;margin:18px 0 42px}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{background:#fff;border:1px solid var(--line);padding:30px;min-height:255px}
.icon{color:var(--accent);font-family:Oswald,sans-serif;font-size:1.5rem}
.card h3{font-size:1.3rem;margin:12px 0 8px}.card p{color:var(--muted);margin:0}
.dark{background:#171a19;color:#fff}.dark .eyebrow{color:#d98a4c}.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:70px}.about-grid p{color:#c7cdca}.text-link{display:inline-block;color:#fff;text-decoration:none;font-weight:700;border-bottom:1px solid var(--accent);padding-bottom:4px;margin-top:10px}
.contact{background:#e9e5dc}.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:start}.contact-box{background:#fff;border:1px solid var(--line);padding:30px}.contact-box a,.contact-box div{display:block;color:var(--ink);text-decoration:none;padding:15px 0;border-bottom:1px solid var(--line);font-weight:600;overflow-wrap:anywhere}.contact-box a:last-child,.contact-box div:last-child{border-bottom:0}.contact-box span{display:block;color:var(--accent);font-size:.7rem;letter-spacing:.15em;font-weight:700;margin-bottom:4px}
footer{background:#101211;color:#9da4a0}.footer{display:flex;justify-content:space-between;gap:20px;padding:25px 0;font-size:.82rem}
@media(max-width:750px){
 .nav-call{font-size:.85rem}.hero{min-height:590px}.trust-grid,.cards,.about-grid,.contact-grid{grid-template-columns:1fr}.trust-grid div{border-right:0;border-bottom:1px solid var(--line)}.section{padding:72px 0}.footer{display:block}.footer p:last-child{margin-top:4px}
}
</body>
</html>
