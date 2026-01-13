---
title: "Ralf Schmaelzle"
hidemeta: true
layout: "full" 
---

<div class="gateway-container">

<div class="gateway-box suit-side">
<h2>Academic</h2>
<p>Associate Professor<br>Michigan State University</p>
<div class="gateway-links">
<a href="/cv/">Curriculum Vitae &rarr;</a>
<a href="/publications/">Publications &rarr;</a>
</div>
</div>

<div class="gateway-box hoodie-side">
<h2>Studio Evergreen</h2>
<p>Digital Atelier<br>Code, Fiction & VR</p>
<div class="gateway-links">
<a href="/studio/">Enter The Studio &rarr;</a>
</div>
</div>

</div>

<style>
.gateway-container {
display: flex;
flex-wrap: wrap;
gap: 2rem;
justify-content: center;
margin-top: 2rem;
}
.gateway-box {
flex: 1;
min-width: 300px;
padding: 3rem 2rem;
border: 1px solid var(--border);
border-radius: 8px;
text-align: center;
transition: transform 0.2s;
background: var(--entry);
}
.gateway-box:hover {
transform: translateY(-5px);
box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
.hoodie-side { 
background: #1a1a1a; 
color: #fff; 
}
.hoodie-side h2, .hoodie-side p { color: #fff; }
.hoodie-side a { color: #4db6ac; font-weight: bold; text-decoration: none; }
.suit-side a { font-weight: bold; text-decoration: none; color: var(--primary); }
.gateway-links {
display: flex;
flex-direction: column;
gap: 1rem;
margin-top: 2rem;
font-size: 1.1rem;
}
</style>