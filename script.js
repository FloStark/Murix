/* =====================================================
   MURIX – Interactive JavaScript
   Canvas Animation, Scroll Effects, Counters
   ===================================================== */

document.addEventListener('DOMContentLoaded', () => {
    initCanvas();
    initNavbar();
    initHamburger();
    initRevealAnimations();
    initCounters();
    initSmoothScroll();
    initContactForm();
});

/* ============ HERO CANVAS – River/Particle Animation ============ */
function initCanvas() {
    const canvas = document.getElementById('heroCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    let width, height;
    let particles = [];
    let waves = [];
    let mouse = { x: -1000, y: -1000 };
    let animationId;

    function resize() {
        width = canvas.width = canvas.offsetWidth;
        height = canvas.height = canvas.offsetHeight;
    }

    resize();
    window.addEventListener('resize', resize);

    // Particles
    class Particle {
        constructor() {
            this.reset();
        }

        reset() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.size = Math.random() * 2 + 0.5;
            this.speedX = (Math.random() - 0.5) * 0.5;
            this.speedY = (Math.random() - 0.5) * 0.3;
            this.opacity = Math.random() * 0.5 + 0.1;
            this.pulseSpeed = Math.random() * 0.02 + 0.005;
            this.pulseOffset = Math.random() * Math.PI * 2;
        }

        update(time) {
            this.x += this.speedX;
            this.y += this.speedY;

            // Mouse interaction
            const dx = mouse.x - this.x;
            const dy = mouse.y - this.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 150) {
                const force = (150 - dist) / 150;
                this.x -= dx * force * 0.02;
                this.y -= dy * force * 0.02;
            }

            // Wrap around
            if (this.x < -10) this.x = width + 10;
            if (this.x > width + 10) this.x = -10;
            if (this.y < -10) this.y = height + 10;
            if (this.y > height + 10) this.y = -10;

            // Pulse
            this.currentOpacity = this.opacity + Math.sin(time * this.pulseSpeed + this.pulseOffset) * 0.15;
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(0, 229, 255, ${this.currentOpacity})`;
            ctx.fill();
        }
    }

    // Create particles
    const particleCount = Math.min(Math.floor((width * height) / 8000), 120);
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }

    // Wave lines
    class Wave {
        constructor(yOffset, amplitude, speed, opacity) {
            this.yOffset = yOffset;
            this.amplitude = amplitude;
            this.speed = speed;
            this.opacity = opacity;
            this.phase = Math.random() * Math.PI * 2;
        }

        draw(time) {
            ctx.beginPath();
            const baseY = height * this.yOffset;
            for (let x = 0; x <= width; x += 3) {
                const y = baseY +
                    Math.sin((x * 0.003) + (time * this.speed * 0.001) + this.phase) * this.amplitude +
                    Math.sin((x * 0.007) + (time * this.speed * 0.0005)) * (this.amplitude * 0.5);
                if (x === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.strokeStyle = `rgba(0, 229, 255, ${this.opacity})`;
            ctx.lineWidth = 1;
            ctx.stroke();
        }
    }

    waves = [
        new Wave(0.3, 30, 0.8, 0.04),
        new Wave(0.45, 40, 0.6, 0.03),
        new Wave(0.6, 35, 1.0, 0.05),
        new Wave(0.75, 25, 0.7, 0.03),
        new Wave(0.85, 20, 0.9, 0.02),
    ];

    // Draw connections
    function drawConnections() {
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 120) {
                    const opacity = (1 - dist / 120) * 0.15;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = `rgba(0, 229, 255, ${opacity})`;
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }
            }
        }
    }

    // Animate
    let time = 0;
    function animate() {
        time++;
        ctx.clearRect(0, 0, width, height);

        // Draw waves
        waves.forEach(wave => wave.draw(time));

        // Update & draw particles
        particles.forEach(p => {
            p.update(time);
            p.draw();
        });

        // Draw connections
        drawConnections();

        animationId = requestAnimationFrame(animate);
    }

    animate();

    // Mouse tracking
    canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouse.x = e.clientX - rect.left;
        mouse.y = e.clientY - rect.top;
    });

    canvas.addEventListener('mouseleave', () => {
        mouse.x = -1000;
        mouse.y = -1000;
    });
}

/* ============ NAVBAR SCROLL ============ */
function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
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
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    }, { passive: true });
}

/* ============ HAMBURGER MENU ============ */
function initHamburger() {
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');
    if (!hamburger || !navLinks) return;

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
        document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
    });

    // Close menu on link click
    navLinks.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
}

/* ============ SCROLL REVEAL ANIMATIONS ============ */
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
        threshold: 0.1,
        rootMargin: '0px 0px -60px 0px'
    });

    reveals.forEach(reveal => observer.observe(reveal));
}

/* ============ ANIMATED COUNTERS ============ */
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
    const startValue = 0;

    function easeOutQuart(t) {
        return 1 - Math.pow(1 - t, 4);
    }

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easedProgress = easeOutQuart(progress);
        const currentValue = Math.floor(startValue + (target - startValue) * easedProgress);

        element.textContent = currentValue;

        if (progress < 1) {
            requestAnimationFrame(update);
        }
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
                const targetPosition = targetEl.offsetTop - navHeight;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
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

        // Success animation
        btn.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20 6 9 17 4 12"/>
            </svg>
            <span>Gesendet!</span>
        `;
        btn.style.pointerEvents = 'none';

        setTimeout(() => {
            btn.innerHTML = originalContent;
            btn.style.pointerEvents = '';
            form.reset();
        }, 3000);
    });
}

/* ============ PARALLAX ELEMENTS ============ */
window.addEventListener('scroll', () => {
    const scrollY = window.pageYOffset;

    // Hero parallax
    const heroContent = document.querySelector('.hero-content');
    if (heroContent && scrollY < window.innerHeight) {
        heroContent.style.transform = `translateY(${scrollY * 0.15}px)`;
        heroContent.style.opacity = 1 - (scrollY / (window.innerHeight * 0.8));
    }

    // Scroll indicator fade
    const scrollIndicator = document.querySelector('.scroll-indicator');
    if (scrollIndicator) {
        scrollIndicator.style.opacity = 1 - (scrollY / 200);
    }
}, { passive: true });
