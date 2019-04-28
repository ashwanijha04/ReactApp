// eslint-disable-next-line
import React, { Component } from 'react';
import './App.css';
import NavBar from "views/NavBar.js";
import PageHeader from "views/PageHeader.js";
//import 'access-control-allow-origin';






class App extends React.Component {

  state = {
    data : null
  };


    componentWillUnmount() {
      document.body.classList.toggle("index-page");
    }


  componentDidMount() {
    document.body.classList.toggle("index-page");
  }


  render() {
    return (
      <>

      <NavBar/>
      <div className="wrapper">
        <PageHeader />
      </div>


      </>
    );
  }

}



export default App;
