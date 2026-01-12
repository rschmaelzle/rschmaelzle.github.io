---
title: "Ralf Schmaelzle"
hidemeta: true
layout: "full" 
---

<div class="gateway-container">

  <!-- THE SUIT (Left Side) -->
  <div class="gateway-box suit-side">
    <img src="https://via.placeholder.com/300x300/dddddd/333333?text=The+Academic" alt="Professional" class="gateway-img">
    <h2>The Academic</h2>
    <p>Associate Professor<br>Michigan State University</p>
    
    <div class="gateway-links">
        <a href="/cv/">Curriculum Vitae &rarr;</a>
        <a href="/publications/">Publications &rarr;</a>
    </div>
  </div>

  <!-- THE HOODIE (Right Side) -->
  <div class="gateway-box hoodie-side">
    <img src="https://via.placeholder.com/300x300/111111/eeeeee?text=The+Creator" alt="Creative" class="gateway-img">
    <h2>Studio Evergreen</h2>
    <p>Digital Atelier<br>Code, Fiction & VR</p>
    
    <div class="gateway-links">
        <a href="/studio/">Enter The Studio &rarr;</a>
    </div>
  </div>

</div>

<!-- CSS for the Gateway (Paste this directly into the markdown file at the bottom) -->
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
    padding: 2rem;
    border: 1px solid var(--border);
    border-radius: 8px;
    text-align: center;
    transition: transform 0.2s;
}
.gateway-box:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
.gateway-img {
    width: 150px;
    height: 150px;
    object-fit: cover;
    border-radius: 50%; /* Circle Image */
    margin-bottom: 1rem;
    border: 3px solid var(--primary);
}
.suit-side { background: var(--entry); }
.hoodie-side { 
    background: #1a1a1a; 
    color: #fff; 
}
.hoodie-side a { color: #4db6ac; } /* Teal links for contrast */
.gateway-links {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-top: 1.5rem;
    font-weight: bold;
}
</style>