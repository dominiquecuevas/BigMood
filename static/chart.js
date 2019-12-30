var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['anger', 
                'contempt', 
                'disgust', 
                'fear', 
                'happiness', 
                'neutral', 
                'sadness', 
                'surprise'],
        datasets: [{
            data: [.1, 
                    .2, 
                    .3, 
                    .1, 
                    .1, 
                    .2, 
                    .2, 
                    .1],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, .2)',
                'rgba(75, 192, 192, .2)',
                'rgba(205, 133, 63, .2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(105, 101, 90, .2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, .2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(205, 133, 63, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(105, 101, 90, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(153, 102, 255, 1)'
            ]
        }]
    },
    options: {

    }
});

$('#face').on('submit', (evt) => {
    evt.preventDefault();
    const image_url = $('input[name="image_url"]').val();
    // const image_url = "https://us-east-1.tchyn.io/snopes-production/uploads/2016/12/sad-keanu.jpg"
    $.get(`/face.json?image_url=${image_url}`, (res) => {
        myChart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
        });
        // myChart.update();
        myChart.data.datasets[0].data = [
            res.anger, 
            res.contempt, 
            res.disgust, 
            res.fear, 
            res.happiness, 
            res.neutral, 
            res.sadness, 
            res.surprise];
        myChart.update();
    })
});