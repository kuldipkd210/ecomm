import React, { useState } from 'react';
import ProductList from './components/productList.js';
import ProductDetail from './components/productDetail.js';
import './App.css'
function App() {
  const [selectedProduct, setSelectedProduct] = useState(null);

  return (
    <div>
      <h1>Product Catalog</h1>
      {!selectedProduct ? (
        <ProductList onSelectProduct={setSelectedProduct} />
      ) : (
        <ProductDetail product={selectedProduct} goBack={() => setSelectedProduct(null)} />
      )}
    </div>
  );
}

export default App;
