import React from 'react';

function ProductDetail({ product, goBack }) {
  return (
    <div>
      <button onClick={goBack}>Back</button>
      <h2>{product.name}</h2>
      <p>Price: ₹{product.price}</p>
      <p>Description: {product.description}</p>
    </div>
  );
}

export default ProductDetail;
