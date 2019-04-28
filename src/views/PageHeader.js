import React from "react";
// import {Button} from 'reactstrap';
// import classnames from "classnames";
import LoadingBar from 'views/LoadingBar';


// reactstrap components
import { Container } from "reactstrap";
import InputBar from "views/InputBar.js";



class PageHeader extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      formModal: false,
    };
  }

  toggleModal = modalState => {
    this.setState({
      [modalState]: !this.state[modalState]
    });

  };

  render() {
    return (
      <div className="page-header header-filter">
        <div className="squares square1" />
        <div className="squares square2" />
        <div className="squares square3" />
        <div className="squares square4" />
        <div className="squares square5" />
        <div className="squares square6" />
        <div className="squares square7" />

        <Container>
          <div className="content-center brand">
          <InputBar/>

          <h1 className="result">  </h1>
          </div>
        </Container>
      </div>
    );
  }
}



export default PageHeader;
