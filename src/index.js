
//import './index.css';
import App from './App';
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";

//import "assets/scss/blk-design-system-react.scss"
//import "assets/css/nucleo-icons.css";
//import "assets/demo/demo.css";
import "assets/scss/blk-design-system-react.scss?v=1.0.0";



ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route path="/" render={props => <App {...props} />} />
      <Route
        path="/"
        render={props => <App {...props} />}
        // eslint-disable-next-line
      />
      // eslint-disable-next-line
      //<Redirect from="/" to="/components" />
    </Switch>
  </BrowserRouter>,
  document.getElementById("root")
);
