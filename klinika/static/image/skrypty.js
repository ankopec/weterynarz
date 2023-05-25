function usun_zadanie() {
    let zadanie_id = this.dataset['zadanie_id'];
    console.log('usuwam zadanie ', zadanie_id);

    location.href = '/zadanie/usun/' + zadanie_id + '/';
}

let przyciski = document.getElementsByClassName('usun-zadanie');
console.log(przyciski);
for (let p of przyciski) {
    p.addEventListener('click', usun_zadanie);
}

const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });