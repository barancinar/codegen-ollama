/**
 * Kod kopyalama fonksiyonu
 */
function copyCode() {
    const codeElement = document.querySelector('pre code');
    if (codeElement) {
        const textArea = document.createElement('textarea');
        textArea.value = codeElement.textContent;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        
        const copyBtn = document.querySelector('.copy-btn');
        const originalIcon = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="fas fa-check"></i>';
        setTimeout(() => {
            copyBtn.innerHTML = originalIcon;
        }, 2000);
    }
}

/**
 * Sayfa yüklendiğinde çalışacak fonksiyonlar
 */
document.addEventListener('DOMContentLoaded', function() {
    // Form gönderim animasyonu
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>İşleniyor...';
                submitBtn.disabled = true;
            }
        });
    }
    
    // Kod vurgulama işlemini başlat (PrismJS otomatik olarak yapıyor)
    if (typeof Prism !== 'undefined') {
        Prism.highlightAll();
    }
});