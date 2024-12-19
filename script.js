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
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-api-key': apiKey
            },
            body: JSON.stringify(query)
        };

        fetch(`${url}/assets/${datasetId}/${revisionId}/${assetId}`, options)
            .then(response => response.json())
            .then(data => {
                const movie = data.data.title.ratingsSummary.aggregateRating;
                result.textContent = `Recommended Movie: ${movie}`;
            })
            .catch(error => console.error('Error:', error));
    }

    document.querySelector('button').addEventListener('click', chat);
    chatInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            chat();
        }
    });
});
