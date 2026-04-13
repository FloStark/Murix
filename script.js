/* =====================================================
   MURIX – Interactive JavaScript
   Custom Cursor, FAQ, Scroll Effects, Counters
   ===================================================== */

document.addEventListener('DOMContentLoaded', () => {
    initCustomCursor();
    initNavbar();
    initHamburger();
    initRevealAnimations();
    initCounters();
    initSmoothScroll();
    initFAQ();
    initContactForm();
    initMagneticButtons();
    initHeroAnimations();
});

/* ============ CUSTOM CURSOR ============ */
function initCustomCursor() {
    const dot = document.getElementById('cursorDot');
    const ring = document.getElementById('cursorRing');
    if (!dot || !ring) return;

    // Hide on touch devices
    if ('ontouchstart' in window) {
        dot.style.display = 'none';
        ring.style.display = 'none';
        return;
    }

    let mouseX = 0, mouseY = 0;
    let ringX = 0, ringY = 0;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        dot.style.left = mouseX + 'px';
        dot.style.top = mouseY + 'px';
    });

    // Smooth ring follow
    function animateRing() {
        ringX += (mouseX - ringX) * 0.15;
        ringY += (mouseY - ringY) * 0.15;
        ring.style.left = ringX + 'px';
        ring.style.top = ringY + 'px';
        requestAnimationFrame(animateRing);
    }
    animateRing();

    // Hover effects on interactive elements
    const interactives = document.querySelectorAll('a, button, input, select, textarea, .service-card, .vorteil-card, .portfolio-card, .testimonial-card, .pricing-card, .pain-card, .faq-question');

    interactives.forEach(el => {
        el.addEventListener('mouseenter', () => {
            dot.classList.add('hover');
            ring.classList.add('hover');
        });
        el.addEventListener('mouseleave', () => {
            dot.classList.remove('hover');
            ring.classList.remove('hover');
        });
    });

    // Click effect
    document.addEventListener('mousedown', () => dot.classList.add('clicking'));
    document.addEventListener('mouseup', () => dot.classList.remove('clicking'));
}

/* ============ MAGNETIC BUTTONS ============ */
function initMagneticButtons() {
    const magnetics = document.querySelectorAll('.magnetic');

    if ('ontouchstart' in window) return;

    magnetics.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            btn.style.transform = `translate(${x * 0.2}px, ${y * 0.2}px)`;
        });

        btn.addEventListener('mouseleave', () => {
            btn.style.transform = '';
        });
    });
}

/* ============ NAVBAR ============ */
function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }, { passive: true });

    // Active link highlighting
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 200;
            if (window.pageYOffset >= sectionTop) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.style.color = '';
            if (link.getAttribute('href') === '#' + current) {
                if (!link.classList.contains('nav-cta')) {
                    link.style.color = '#00b8d4';
                }
            }
        });
    }, { passive: true });
}

/* ============ HAMBURGER ============ */
function initHamburger() {
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');
    if (!hamburger || !navLinks) return;

    hamburger.addEventListener('click', () => {
        const isActive = hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
        hamburger.setAttribute('aria-expanded', isActive);
        document.body.style.overflow = isActive ? 'hidden' : '';
    });

    // Mobile dropdown toggle
    const dropdowns = document.querySelectorAll('.nav-dropdown');
    dropdowns.forEach(dd => {
        const link = dd.querySelector('.nav-link');
        link.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                dd.classList.toggle('open');
            }
        });
    });

    navLinks.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            // Don't close for dropdown parent on mobile
            if (window.innerWidth <= 768 && link.closest('.nav-dropdown')) return;
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
            document.body.style.overflow = '';
        });
    });

    // Close on dropdown link click (mobile)
    navLinks.querySelectorAll('.dropdown-menu a').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
}

/* ============ SCROLL REVEALS ============ */
function initRevealAnimations() {
    const reveals = document.querySelectorAll('.reveal');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.delay || 0;
                setTimeout(() => {
                    entry.target.classList.add('revealed');
                }, parseInt(delay));
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.08,
        rootMargin: '0px 0px -40px 0px'
    });

    reveals.forEach(reveal => observer.observe(reveal));
}

/* ============ COUNTERS ============ */
function initCounters() {
    const counters = document.querySelectorAll('[data-target]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = parseInt(el.getAttribute('data-target'));
                animateCounter(el, target);
                observer.unobserve(el);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));
}

function animateCounter(element, target) {
    const duration = 2000;
    const startTime = performance.now();

    function easeOutQuart(t) { return 1 - Math.pow(1 - t, 4); }

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentValue = Math.floor(target * easeOutQuart(progress));
        element.textContent = currentValue;
        if (progress < 1) requestAnimationFrame(update);
    }

    requestAnimationFrame(update);
}

/* ============ SMOOTH SCROLL ============ */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetEl = document.querySelector(targetId);
            if (targetEl) {
                const navHeight = document.querySelector('.navbar').offsetHeight;
                window.scrollTo({
                    top: targetEl.offsetTop - navHeight,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/* ============ FAQ ACCORDION ============ */
function initFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            // Close all
            faqItems.forEach(i => i.classList.remove('active'));

            // Toggle current
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });
}

/* ============ CONTACT FORM ============ */
function initContactForm() {
    const form = document.getElementById('contactForm');
    if (!form) return;

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const btn = form.querySelector('button[type="submit"]');
        const originalContent = btn.innerHTML;

        btn.innerHTML = `<span>Sende...</span>`;
        btn.style.pointerEvents = 'none';

        const formData = new FormData(form);

        fetch("https://formsubmit.co/ajax/hello@murix.at", {
            method: "POST",
            headers: {
                'Accept': 'application/json'
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            btn.innerHTML = `
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="20 6 9 17 4 12"/>
                </svg>
                <span>Gesendet!</span>
            `;
            btn.style.background = '#22c55e';

            setTimeout(() => {
                btn.innerHTML = originalContent;
                btn.style.pointerEvents = '';
                btn.style.background = '';
                form.reset();
            }, 3000);
        })
        .catch(error => {
            btn.innerHTML = `<span>Ein Fehler ist aufgetreten!</span>`;
            btn.style.background = '#ef4444';
            
            setTimeout(() => {
                btn.innerHTML = originalContent;
                btn.style.pointerEvents = '';
                btn.style.background = '';
            }, 3000);
        });
    });
}

/* ============ PARALLAX ============ */
window.addEventListener('scroll', () => {
    const scrollY = window.pageYOffset;

    // Hero parallax
    const heroContent = document.querySelector('.hero-content');
    if (heroContent && scrollY < window.innerHeight) {
        heroContent.style.transform = `translateY(${scrollY * 0.1}px)`;
        heroContent.style.opacity = 1 - (scrollY / (window.innerHeight * 0.9));
    }

    // Scroll indicator fade
    const scrollIndicator = document.querySelector('.scroll-indicator');
    if (scrollIndicator) {
        scrollIndicator.style.opacity = 1 - (scrollY / 200);
    }
}, { passive: true });

/* ============ HERO ANIMATIONS ============ */
function initHeroAnimations() {
    initTypewriter();
    initParticles();
    initHeroParallax();
}

function initTypewriter() {
    const el = document.getElementById('typewriter');
    if (!el) return;

    const phrases = [' Websites', ' IT-Systeme', ' SEO-Strategien'];
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typeSpeed = 150;

    function type() {
        const currentPhrase = phrases[phraseIndex];
        
        if (isDeleting) {
            el.textContent = currentPhrase.substring(0, charIndex - 1);
            charIndex--;
            typeSpeed = 100;
        } else {
            el.textContent = currentPhrase.substring(0, charIndex + 1);
            charIndex++;
            typeSpeed = 200;
        }

        if (!isDeleting && charIndex === currentPhrase.length) {
            isDeleting = true;
            typeSpeed = 2000; // Pause at end
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            typeSpeed = 500;
        }

        setTimeout(type, typeSpeed);
    }

    type();
}

function initParticles() {
    const container = document.getElementById('heroParticles');
    if (!container) return;

    const symbols = ['✦', '+', '×', '•'];
    const particleCount = 15;

    for (let i = 0; i < particleCount; i++) {
        const p = document.createElement('span');
        p.className = 'particle';
        p.textContent = symbols[Math.floor(Math.random() * symbols.length)];
        
        // Random position
        p.style.left = Math.random() * 100 + '%';
        p.style.top = Math.random() * 100 + '%';
        
        // Random animation properties
        const duration = 3 + Math.random() * 4;
        const delay = Math.random() * 5;
        p.style.setProperty('--duration', `${duration}s`);
        p.style.setProperty('--delay', `${delay}s`);
        p.style.animation = `float-particle ${duration}s ease-in-out infinite ${delay}s`;

        container.appendChild(p);
    }
}

function initHeroParallax() {
    const hero = document.getElementById('hero');
    if (!hero) return;

    const orbs = document.querySelectorAll('.hero-gradient-orb');

    hero.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth) - 0.5;
        const y = (e.clientY / window.innerHeight) - 0.5;

        orbs.forEach((orb, index) => {
            const factor = (index + 1) * 20;
            orb.style.transform = `translate(${x * factor}px, ${y * factor}px)`;
        });
    });
}
