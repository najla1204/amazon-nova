document.addEventListener('DOMContentLoaded', () => {
    const runBtn = document.getElementById('runWorkflow');
    const runAgentBtn = document.getElementById('runAgent');
    const messageInput = document.getElementById('message');
    const fileInput = document.getElementById('document');
    const fileNameDisplay = document.getElementById('fileName');
    const resultContent = document.getElementById('resultContent');
    const loader = document.getElementById('loader');
    const statusIndicator = document.getElementById('statusIndicator');
    const stepTags = document.getElementById('stepTags');

    // Update filename when a file is selected
    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        fileNameDisplay.textContent = file ? file.name : 'No file selected';
    });

    const clearResults = () => {
        resultContent.innerHTML = '';
        statusIndicator.classList.add('hidden');
        statusIndicator.className = 'status-badge hidden';
        stepTags.classList.add('hidden');
        stepTags.innerHTML = '';
    };

    const handleWorkflow = async (endpoint) => {
        const message = messageInput.value.trim();
        const file = fileInput.files[0];

        if (!message) {
            alert('Please enter a request.');
            return;
        }

        clearResults();
        loader.classList.remove('hidden');

        try {
            const payload = {
                message: message,
                document_name: file ? file.name : "none"
            };

            const response = await fetch(`http://127.0.0.1:8000${endpoint}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.statusText}`);
            }

            const data = await response.json();
            
            if (endpoint === '/ai-agent') {
                renderAgentResults(data);
            } else {
                resultContent.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
            }
        } catch (error) {
            resultContent.innerHTML = `<p style="color: #ef4444;">Error: ${error.message}</p>`;
        } finally {
            loader.classList.add('hidden');
        }
    };

    const renderAgentResults = (data) => {
        // Show status
        statusIndicator.classList.remove('hidden');
        if (data.status === "success") {
            statusIndicator.textContent = "Workflow Successful";
            statusIndicator.classList.add("success");
        } else {
            statusIndicator.textContent = "Analysis Complete";
            statusIndicator.classList.add("info");
        }

        // Render JSON
        resultContent.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;

        // Render Step Tags
        if (data.steps_completed && data.steps_completed.length > 0) {
            stepTags.classList.remove('hidden');
            data.steps_completed.forEach(step => {
                const tag = document.createElement('span');
                tag.className = 'step-tag';
                tag.textContent = step.replace('_', ' ');
                stepTags.appendChild(tag);
            });
        }
    };

    runBtn.addEventListener('click', () => handleWorkflow('/run-workflow'));
    runAgentBtn.addEventListener('click', () => handleWorkflow('/ai-agent'));
});
