document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('formulario');
    const pdfInput = document.getElementById('pdfs');
    const pdfDisplay = document.getElementById('pdfs-display');
    const excelInput = document.getElementById('excel');
    const excelDisplay = document.getElementById('excel-display');
    const smtpToggle = document.getElementById('smtp-toggle');
    const smtpOption = document.getElementById('smtp-option');
    const btnEnviar = document.getElementById('btn-enviar');

    if (pdfInput) {
        pdfInput.addEventListener('change', function() {
            const files = this.files;
            if (files.length > 0) {
                const names = Array.from(files).map(f => f.name).join(', ');
                pdfDisplay.textContent = files.length + ' archivo(s) seleccionado(s)';
                pdfDisplay.classList.add('has-value');
            }
        });
    }

    if (excelInput) {
        excelInput.addEventListener('change', function() {
            if (this.files.length > 0) {
                excelDisplay.textContent = this.files[0].name;
                excelDisplay.classList.add('has-value');
            }
        });
    }

    if (smtpToggle) {
        smtpToggle.addEventListener('change', function() {
            if (this.checked) {
                smtpOption.classList.add('active');
            } else {
                smtpOption.classList.remove('active');
            }
        });
    }

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const tutor = document.getElementById('tutor').value.trim();
            const emailTutor = document.getElementById('email-tutor').value.trim();
            const password = document.getElementById('password').value;
            const pdfs = pdfInput.files.length;
            const excel = excelInput.files.length;

            if (!tutor || !emailTutor || !password || !pdfs || !excel) {
                alert('Por favor, complete todos los campos obligatorios.');
                return;
            }

            const progreso = document.getElementById('progreso');
            if (!progreso) {
                const progDiv = document.createElement('div');
                progDiv.id = 'progreso';
                progDiv.style.cssText = 'margin-top:1rem;padding:1rem;background:#f0f0f0;border-radius:8px;';
                progDiv.innerHTML = '<div id="progreso-bar" style="height:20px;background:#1a3a6e;border-radius:4px;width:0%;transition:width 0.3s;"></div><p id="progreso-texto" style="text-align:center;margin-top:0.5rem;">Iniciando...</p>';
                form.appendChild(progDiv);
            }

            const progBar = document.getElementById('progreso-bar');
            const progTexto = document.getElementById('progreso-texto');

            btnEnviar.disabled = true;
            btnEnviar.textContent = 'Enviando...';

            const formData = new FormData(form);

            let totalEnviados = 0;
            const totalPDFs = pdfs;

            const intervalo = setInterval(() => {
                if (totalEnviados < totalPDFs) {
                    totalEnviados++;
                    const porcentaje = Math.round((totalEnviados / totalPDFs) * 100);
                    progBar.style.width = porcentaje + '%';
                    progTexto.textContent = 'Enviando... ' + totalEnviados + '/' + totalPDFs;
                }
            }, 800);

            fetch('procesar.php', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                clearInterval(intervalo);
                if (data.success) {
                    progBar.style.width = '100%';
                    progTexto.textContent = 'Completado: ' + data.exitos + ' enviados, ' + data.fallos + ' fallos';
                    alert(`Envío completado.\nÉxitos: ${data.exitos}\nFallos: ${data.fallos}`);
                    form.reset();
                    pdfDisplay.textContent = 'Seleccione los PDFs (puede seleccionar varios)';
                    pdfDisplay.classList.remove('has-value');
                    excelDisplay.textContent = 'Seleccione el archivo Excel';
                    excelDisplay.classList.remove('has-value');
                    const prog = document.getElementById('progreso');
                    if (prog) prog.remove();
                } else {
                    progTexto.textContent = 'Error: ' + data.message;
                    progBar.style.background = '#dc3545';
                    alert('Error: ' + data.message);
                }
            })
            .catch(error => {
                clearInterval(intervalo);
                progTexto.textContent = 'Error de conexión';
                progBar.style.background = '#dc3545';
                alert('Error de conexión: ' + error.message);
            })
            .finally(() => {
                btnEnviar.disabled = false;
                btnEnviar.textContent = 'ENVIAR DOCUMENTOS';
            });
        });
    }

    const inputs = document.querySelectorAll('input[type="text"], input[type="email"], input[type="password"], textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
    });
});

function descargarManual(tipo) {
    console.log('Descargando manual de ' + tipo);
}