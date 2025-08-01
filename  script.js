/*

Valencia Walker's for Jewel.technology


*/

document.addEventListener('DOMContentLoaded', () => {
  fetch('/api/jewelry')
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById('jewelryGrid');
      container.innerHTML = '';
      data.forEach(item => {
        const card = document.createElement('div');
        card.className = 'col-sm-6 col-md-4 col-lg-3 mb-4';
        card.innerHTML = `
          <div class="card shadow-sm h-100">
            <img src="${item.image}" class="card-img-top" alt="${item.name}" />
            <div class="card-body">
              <h5 class="card-title">${item.name}</h5>
              <p class="card-text">${item.category}</p>
              <p class="fw-bold">${item.price}</p>
              <button class="btn btn-outline-warning w-100">Add to Cart</button>
            </div>
          </div>
        `;
        container.appendChild(card);
      });
    });
});
