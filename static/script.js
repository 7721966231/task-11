function startEmotionDetection() {
    fetch('/detect_emotion')
        .then(response => response.json())
        .then(data => {
            document.getElementById('emotion').textContent = data.emotion;
            // Call the Python function to play music
            playMusic(data.emotion);
        });
}

function playMusic(emotion) {
    fetch('/play_music', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ emotion: emotion })
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    const chatInput = document.getElementById('chat-input');
    const result = document.getElementById('result');

    function chat() {
        const genre = chatInput.value.trim();
        if (genre) {
            getRecommendation(genre);
        }
    }

    function getRecommendation(genre) {
        const url = `https://api-fulfill.dataexchange.us-east-1.amazonaws.com/v1`;
        const datasetId = 'your-dataset-id';
        const revisionId = 'your-revision-id';
        const assetId = 'your-asset-id';
        const apiKey = 'your-api-key';

        const query = {
            query: `{
                title(id: "tt0120338") {
                    ratingsSummary {
                        aggregateRating
                        voteCount
                    }
                }
            }`
        };

        const options = {
            method: