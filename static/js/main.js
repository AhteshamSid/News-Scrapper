$(function () {
    var $articlesChart = $("#articles-pie-chart");
    $.ajax({
        url: $articlesChart.data("url"),
        success: function (data) {
            var ctx = $articlesChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Number of Articles',
                        backgroundColor: data.colors,
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'left',
                    },
                    title: {
                        display: true,
                        text: 'A Number of Articles',
                        fontSize: 18,
                        position: 'top',
                    },
                }
            });

        }
    });

});

$(function () {
    var $articlesChart = $("#articles-bar-chart");
    $.ajax({
        url: $articlesChart.data("url"),
        success: function (data) {
            var ctx = $articlesChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Number of Articles',
                        backgroundColor: data.colors,
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'A Number of Articles in descending order',
                        fontSize: 18,
                        position: 'top',
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });

        }
    });

});

$(function () {
    var $articlesChart = $("#top-en-word-chart");
    $.ajax({
        url: $articlesChart.data("url"),
        success: function (data) {
            var ctx = $articlesChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Amount',
                        backgroundColor: data.colors,
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Top English Words',
                        fontSize: 18,
                        position: 'top',
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });

        }
    });

});

$(function () {
    var $articlesChart = $("#top-pl-word-chart");
    $.ajax({
        url: $articlesChart.data("url"),
        success: function (data) {
            var ctx = $articlesChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Amount',
                        backgroundColor: data.colors,
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Top Polish Words',
                        fontSize: 18,
                        position: 'top',
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });

        }
    });

});

