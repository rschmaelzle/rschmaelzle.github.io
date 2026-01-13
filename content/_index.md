---
title: "Ralf Schmälzle"
hidemeta: true
description: "Ph.D. / Assoc. Prof. - Michigan State University"
---

<!-- LOAD TYPER JS -->
<script async src="https://unpkg.com/typer-dot-js@0.1.0/typer.js"></script>

<div class="profile-container">

  <!-- LEFT COLUMN: BIO & LINKS -->
  <div class="profile-sidebar">
    
    <!-- Profile Image -->
    <img src="http://www.ralfschmaelzle.net/wp-content/uploads/2023/04/AudienceBrain.jpg" alt="Ralf Schmälzle" class="profile-img">
    
    <h3>Ralf Schmälzle, Ph.D.</h3>
    <p class="role">Assoc. Prof.</p>

    <!-- Typer Animation -->
    <div class="typer-container">
      <span class="typer" id="first-typer" 
            data-delay="50" 
            data-words="SHMAL-ts-lee, 拉尔夫·舒梅尔茨勒, ラルフ・シュメルツレ, رالف شمالتسل, राल्फ श्मेल्ज़ले, Rælf ʃmɛlt͡slə, Ральф Шмельцле, राल्फ श्मेल्ज़ले, Ραλφ Σμέλτσλε, 랄프 셈맬츌레" 
            data-colors="#18453b,#069A6D,#008208,#000000,#7BBD00">
      </span>
      <span class="cursor" data-owner="first-typer"></span>
    </div>

    <!-- Affiliation Links -->
    <div class="profile-links">
      <a href="http://nomcomm.github.io">Neuroscience of Messages Lab</a>
      <a href="http://carismalab.com">Carismalab (VR/AR Center)</a>
      <a href="https://comartsci.msu.edu/ralfschmaelzle">Dept. of Communication</a>
      <a href="http://msu.edu">Michigan State University</a>
    </div>

  </div>

  <!-- RIGHT COLUMN: WELCOME TEXT -->
  <div class="profile-content">
    
    <h2>Welcome!</h2>
    
    <p>I study <strong>communication neuroscience</strong>. This involves a radically interdisciplinary approach that integrates theories from communication science, cognitive neuroscience, and psychology.</p>
    
    <p>My goal is to find out how the human brain responds to messages and how brain activity relates to message effects. Much of my work focuses on:</p>

    <ul>
      <li>
        <strong>Media Neuroscience and Mass Communication</strong><br>
        <small>(e.g.: How do mass media collectively engage the brains of audience members? How do we respond to movies and stories?)</small>
      </li>
      <li>
        <strong>Neuroimaging of Health and Risk Communication</strong><br>
        <small>(e.g.: Can we predict whether a message will work and for whom? Can we detect neural signatures of attention, personal relevance, or affective evaluation?)</small>
      </li>
    </ul>

    <p>Two cross-cutting themes that play a large role in my current work are <strong>Virtual Reality</strong> — the communication medium of the future — and <strong>Artificial Intelligence</strong> — the quest to build machines that can think, act, and communicate like humans.</p>

    <p><em>Thanks for your interest in my work, and for visiting this site.</em></p>

  </div>

</div>

<!-- CSS STYLING -->
<style>
/* Grid Layout: 35% Left, 65% Right */
.profile-container {
    display: grid;
    grid-template-columns: 1fr 2fr; /* 1 part left, 2 parts right */
    gap: 3rem;
    margin-top: 2rem;
    align-items: start;
}

/* Sidebar Styling */
.profile-sidebar {
    text-align: center;
    padding: 1.5rem;
    background: var(--entry); /* Matches theme card color */
    border: 1px solid var(--border);
    border-radius: 8px;
}

.profile-img {
    border-radius: 50%; /* Circle */
    width: 180px;
    height: 180px;
    object-fit: cover;
    margin-bottom: 1rem;
    border: 4px solid var(--primary);
}

.typer-container {
    margin: 1rem 0;
    font-weight: bold;
    min-height: 1.5em; /* Prevents jumping */
    color: var(--primary);
}

.profile-links {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    font-size: 0.9rem;
    margin-top: 1.5rem;
}

.profile-links a {
    text-decoration: none;
    font-weight: 500;
}

/* Content Styling */
.profile-content h2 {
    margin-top: 0;
}

.profile-content ul {
    margin-top: 1rem;
    padding-left: 1.2rem;
}

.profile-content li {
    margin-bottom: 1rem;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
    .profile-container {
        grid-template-columns: 1fr; /* Stack vertically on phones */
        gap: 2rem;
    }
}
</style>