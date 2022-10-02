import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";

import './App.css';
import Splash from './components/splash/Splash';

import HomePage from './pages/Home';
import Page404 from './pages/404';
class App extends Component {
  state = {
    isLoading: false
  }
  componentDidMount() {
    this.setState(
      {isLoading: true}
    )
    setTimeout(() => {
      this.setState(
        { isLoading: false }
      );
    }, 5000)
  }
  render() { 
    return (
      <Router>
        <div className="container">
          {this.state.isLoading ? <Splash />: null}
          <Routes>
            <Route exact path="/" element={
              <HomePage />
            } />
            <Route path="*" element={
              <Page404 />
            } />
          </Routes>
        </div>
      </Router >
    );
  }
}
 
export default App;
