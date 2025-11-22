document.addEventListener('DOMContentLoaded', function() {

    // --- 1. HELPER: CUSTOM TOAST NOTIFICATION ---
    function showToast(message) {
        const toast = document.getElementById("custom-toast");
        if(toast) {
            toast.innerText = message;
            toast.className = "show";
            // Hide after 3 seconds
            setTimeout(function(){ toast.className = toast.className.replace("show", ""); }, 3000);
        } else {
            // Fallback if HTML missing
            alert(message);
        }
    }

    // --- 2. MARKET COPY CONTACT ---
    window.copyContact = function(btn) {
        const contactInfo = btn.getAttribute('data-contact');
        
        navigator.clipboard.writeText(contactInfo).then(() => {
            const originalText = btn.innerHTML;
            
            // Visual feedback
            btn.innerHTML = '✅ Copied!';
            btn.style.backgroundColor = "var(--laurel)";
            btn.style.color = "white";
            
            showToast("Contact copied to clipboard!"); // Use brand alert

            // Revert after 2 seconds
            setTimeout(() => {
                btn.innerHTML = originalText;
                btn.style.backgroundColor = "";
                btn.style.color = "var(--russet)";
            }, 2000);
        }).catch(err => {
            showToast("Contact: " + contactInfo);
        });
    };

    // --- 3. QUIZ LOGIC ---
    const quizForm = document.getElementById('quiz-form');
    if (quizForm) {
        const allCards = Array.from(document.querySelectorAll('.quiz-card'));
        const deckContainer = document.getElementById('card-deck');
        const progressBar = document.querySelector('.progress-fill');
        
        // Shuffle
        for (let i = allCards.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [allCards[i], allCards[j]] = [allCards[j], allCards[i]];
        }

        // Select 5
        const selectedCards = allCards.slice(0, 5);
        deckContainer.innerHTML = ''; 
        selectedCards.forEach((card, index) => {
            deckContainer.appendChild(card);
            const btn = card.querySelector('button');
            
            if (index === 4) { 
                btn.innerText = "Finish & See Score";
                btn.type = "submit";
                btn.classList.remove('btn-next');
            } else {
                btn.innerText = "Next Question";
                btn.type = "button";
                btn.classList.add('btn-next');
            }
        });

        // Show First
        let currentStep = 0;
        showCard(0);

        function showCard(index) {
            const cards = deckContainer.querySelectorAll('.quiz-card');
            cards.forEach(c => c.classList.remove('active-card'));
            if (cards[index]) {
                cards[index].classList.add('active-card');
                const percent = ((index + 1) / 5) * 100;
                if(progressBar) progressBar.style.width = percent + "%";
                const counter = document.getElementById('q-counter');
                if(counter) counter.innerText = `${index + 1}/5`;
            }
        }

        // Next Button Logic
        deckContainer.addEventListener('click', function(e) {
            if (e.target.classList.contains('btn-next')) {
                const currentCard = e.target.closest('.quiz-card');
                const inputs = currentCard.querySelectorAll('input[type="radio"]');
                let answered = false;
                inputs.forEach(input => { if(input.checked) answered = true; });

                if (!answered) {
                    // USE THE NEW BRAND ALERT
                    showToast("Please select an answer first!");
                    return;
                }
                currentStep++;
                showCard(currentStep);
            }
        });
    }

    // --- 4. SCROLL REVEAL ---
    function reveal() {
        var reveals = document.querySelectorAll('.reveal');
        for (var i = 0; i < reveals.length; i++) {
            var windowheight = window.innerHeight;
            var revealtop = reveals[i].getBoundingClientRect().top;
            var revealpoint = 50; 
            if (revealtop < windowheight - revealpoint) {
                reveals[i].classList.add('active');
            } else {
                reveals[i].classList.add('active'); 
            }
        }
    }
    window.addEventListener('scroll', reveal);
    reveal(); 
});