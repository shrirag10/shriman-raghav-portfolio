// ================================================
//  SHARED JS — Theme Toggle + Mobile Nav
//  Simple Portfolio — Shriman Raghav Srinivasan
// ================================================

(function () {
  const html   = document.documentElement;
  const toggle = document.getElementById('theme-toggle');
  const icon   = document.getElementById('theme-icon');

  // Restore saved theme
  const saved = localStorage.getItem('theme');
  if (saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    html.classList.add('dark');
    html.setAttribute('data-theme', 'dark');
    if (icon) icon.textContent = 'light_mode';
  }

  // Theme toggle
  if (toggle) {
    toggle.addEventListener('click', () => {
      const isDark = html.classList.toggle('dark');
      html.setAttribute('data-theme', isDark ? 'dark' : 'light');
      if (icon) icon.textContent = isDark ? 'light_mode' : 'dark_mode';
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
  }

  // Mobile nav
  const mobileBtn  = document.getElementById('mobile-menu-toggle');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileIcon = document.getElementById('mobile-menu-icon');

  if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener('click', () => {
      const isOpen = mobileMenu.classList.contains('open');
      mobileMenu.classList.toggle('open', !isOpen);
      if (mobileIcon) mobileIcon.textContent = isOpen ? 'menu' : 'close';
    });
  }

  // Project filter chips (used on academic / tesla / hero pages)
  const filterBtns = document.querySelectorAll('.chip[data-filter]');
  const projectItems = document.querySelectorAll('.project-item');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => { b.classList.remove('active'); b.style = ''; });
      btn.classList.add('active');
      const cat = btn.getAttribute('data-filter');
      projectItems.forEach(item => {
        item.style.display = (cat === 'all' || item.getAttribute('data-category') === cat) ? 'flex' : 'none';
      });
    });
  });

  // Project modal (used on academic / tesla / hero pages)
  const modal       = document.getElementById('project-modal');
  const closeBtn    = document.getElementById('close-modal');
  const modalTitle  = document.getElementById('modal-title');
  const modalDesc   = document.getElementById('modal-desc');
  const modalLink   = document.getElementById('modal-link');
  const modalMedia  = document.getElementById('modal-media-container');
  const modalTags   = document.getElementById('modal-tags');
  const modalResults = document.getElementById('modal-results');

  if (modal) {
    const openModal = (data) => {
      if (!data) return;
      if (modalMedia) {
        const mediaSrc = data.video || data.gif || data.img;
        if (!mediaSrc) {
          modalMedia.innerHTML = `<div class="img-placeholder">No preview available</div>`;
        } else if (data.video || mediaSrc.endsWith('.mp4') || mediaSrc.endsWith('.webm')) {
          const vid = data.video || mediaSrc;
          const fallback = data.img ? `<img src="${data.img}" alt="${data.title}" class="w-full h-full object-cover rounded-t-lg"/>` : `<div class="img-placeholder">No preview</div>`;
          modalMedia.innerHTML = `<video src="${vid}" autoplay loop muted playsinline class="w-full h-full object-cover rounded-t-lg" onerror="this.parentElement.innerHTML='${fallback}'"></video>`;
        } else if (mediaSrc.endsWith('.gif')) {
          modalMedia.innerHTML = `<img src="${mediaSrc}" alt="${data.title}" class="w-full h-full object-contain rounded-t-lg"/>`;
        } else {
          modalMedia.innerHTML = `<img src="${mediaSrc}" alt="${data.title}" class="w-full h-full object-cover rounded-t-lg" onerror="this.parentElement.innerHTML='<div class=\\'img-placeholder\\'>No preview available</div>'"/>`;
        }
      }
      
      if (modalTitle) modalTitle.textContent = data.title;
      
      if (modalTags) {
        const tags = data.tags || [];
        modalTags.innerHTML = tags.map(tag => `<span class="px-3 py-1 rounded-full text-xs font-space bg-surface-container-high text-on-surface">${tag}</span>`).join('');
      }

      let overview = data.desc || '';
      let resultsHtml = '';

      // Parse Result from desc if it exists in the old format
      if (overview.includes('Result:')) {
        const parts = overview.split(/<p[^>]*><strong[^>]*>Result:<\/strong>|<p><strong[^>]*>Result:<\/strong>/);
        if (parts.length > 1) {
          overview = parts[0];
          let resultText = parts[1].replace('</p>', '').trim();
          // Split result into sentences
          const sentences = resultText.split('. ').filter(s => s.length > 5);
          resultsHtml = sentences.map(s => `<li>${s}${s.endsWith('.') ? '' : '.'}</li>`).join('');
        }
      } else if (data.keyResults) {
        resultsHtml = data.keyResults.map(r => `<li>${r}</li>`).join('');
      }

      if (modalDesc) {
        modalDesc.innerHTML = overview;
      }
      if (modalResults) {
        modalResults.innerHTML = resultsHtml;
        modalResults.parentElement.style.display = resultsHtml ? 'block' : 'none';
      }

      if (modalLink) {
        if (data.link && data.link !== '#') {
          modalLink.href = data.link;
          modalLink.style.display = 'inline-flex';
        } else {
          modalLink.style.display = 'none';
        }
      }
      modal.classList.add('open');
      modal.style.display = 'flex'; // override display:none
      document.body.style.overflow = 'hidden';
    };

    const closeModal = () => {
      modal.classList.remove('open');
      document.body.style.overflow = '';
      setTimeout(() => {
        modal.style.display = 'none';
        if (modalMedia) modalMedia.innerHTML = '';
      }, 300); // Wait for opacity transition
    };

    // Bind view-details buttons using window.PROJECT_DATA set per-page
    document.querySelectorAll('.view-details').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id   = e.currentTarget.getAttribute('data-id');
        const data = (window.PROJECT_DATA || {})[id];
        openModal(data);
      });
    });

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });
  }
})();
