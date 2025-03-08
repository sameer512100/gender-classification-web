document.getElementById('predict').onclick = () => {
    const imageInput = document.getElementById('image');
    const image = imageInput.files[0];
    if (!image) {
        alert('Please select an image.');
        return;
    }
    const formData = new FormData();
    formData.append('image', image);
    fetch('/', { method: 'POST', body: formData })
        .then(r => r.json())
        .then(data => document.getElementById('result').textContent = data.prediction);
};