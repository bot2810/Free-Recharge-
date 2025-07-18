
document.addEventListener('DOMContentLoaded', function() {
    const nameForm = document.getElementById('nameForm');
    const nameInput = document.getElementById('userName');
    const enterBtn = document.querySelector('.enter-btn');

    // Focus on input when page loads
    nameInput.focus();

    // Handle form submission
    nameForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const userName = nameInput.value.trim();
        
        if (userName.length < 2) {
            showError('Please enter a valid name (at least 2 characters)');
            return;
        }
        
        // Show success animation
        enterBtn.classList.add('success-animation');
        enterBtn.innerHTML = '<span>Processing...</span><span class="btn-icon">⏳</span>';
        
        // Store user name in localStorage
        localStorage.setItem('userName', userName);
        
        // Redirect to main game after short delay
        setTimeout(() => {
            window.location.href = '/game';
        }, 1500);
    });

    // Add enter key support
    nameInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            nameForm.dispatchEvent(new Event('submit'));
        }
    });

    // Input validation and styling
    nameInput.addEventListener('input', function() {
        const value = this.value.trim();
        if (value.length >= 2) {
            this.style.borderColor = '#4ECDC4';
            enterBtn.disabled = false;
        } else {
            this.style.borderColor = '#e0e0e0';
        }
    });

    function showError(message) {
        nameInput.style.borderColor = '#ff6b6b';
        nameInput.style.boxShadow = '0 6px 25px rgba(255, 107, 107, 0.3)';
        
        // Create error message element
        const existingError = document.querySelector('.error-message');
        if (existingError) {
            existingError.remove();
        }
        
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.style.cssText = `
            color: #ff6b6b;
            font-size: 0.9rem;
            margin-top: 10px;
            text-align: center;
            animation: shake 0.5s ease;
        `;
        errorDiv.textContent = message;
        
        nameForm.appendChild(errorDiv);
        
        // Remove error after 3 seconds
        setTimeout(() => {
            if (errorDiv.parentNode) {
                errorDiv.remove();
            }
            nameInput.style.borderColor = '#e0e0e0';
            nameInput.style.boxShadow = '0 4px 15px rgba(0, 0, 0, 0.1)';
        }, 3000);
    }

    // Add shake animation to CSS
    const style = document.createElement('style');
    style.textContent = `
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }
    `;
    document.head.appendChild(style);

    // Add floating particles effect
    createFloatingParticles();
});

function createFloatingParticles() {
    setInterval(() => {
        if (Math.random() < 0.3) {
            const particle = document.createElement('div');
            particle.innerHTML = ['💰', '🎁', '⭐', '🎰'][Math.floor(Math.random() * 4)];
            particle.style.cssText = `
                position: fixed;
                font-size: 1.5rem;
                left: ${Math.random() * 100}%;
                top: 100vh;
                pointer-events: none;
                z-index: -1;
                animation: floatUp 4s linear forwards;
                opacity: 0.6;
            `;
            
            document.body.appendChild(particle);
            
            setTimeout(() => {
                if (particle.parentNode) {
                    particle.remove();
                }
            }, 4000);
        }
    }, 1000);
}

// Add floating animation
const floatUpStyle = document.createElement('style');
floatUpStyle.textContent = `
    @keyframes floatUp {
        0% { 
            transform: translateY(0) rotate(0deg); 
            opacity: 0.6; 
        }
        100% { 
            transform: translateY(-100vh) rotate(360deg); 
            opacity: 0; 
        }
    }
`;
document.head.appendChild(floatUpStyle);
