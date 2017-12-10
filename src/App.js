import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import './css/main.css';

class App extends Component {
  render() {
    return (
      <div>
        <div className="navbar navbar-expand-lg  navbar-dark bg-primary navbar-right">
          <div className="container">
            <a className="navbar-brand" href="#">
              <img src="image/logo B.png" height="30" alt="" />
            </a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarResponsive">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#team">The Team</a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div className="container">
          <div class="bs-docs-section">
            <div class="row">
              <div class="col-lg-6 ">
                <div class="bs-component">
                  <form role="form" id="excel-upload-form" method="post" enctype="multipart/form-data">
                    <fieldset>
                      <legend>Upload New Layout</legend>
                      <div class="form-group">
                        <label for="exampleInputFile">Excel Sheet Input</label>
                        <input type="file" class="form-control-file" id="exampleInputFile" aria-describedby="fileHelp" />
                        <small id="fileHelp" class="form-text text-muted">Please Upload A new excel layout file.</small>
                        <div class="clearfix"></div>
                      </div>
                    </fieldset>
                    <div class="clearfix"></div>
                  </form>
                </div>
              </div>
            </div>
          </div>



          <div class="bs-docs-section">

            <div class="row">
              <div class="col-lg-12">
                <div class="page-header">
                  <h1 id="tables">Tables</h1>
                </div>

                <div class="bs-component">
                  <table class="table table-striped table-hover table-bordered output-table">
                    <thead class="thead-dark">
                      <tr>
                        <th>#</th>
                        <th>Layout Name</th>
                        <th>Match Percentage</th>
                        <th>Accuracy</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>1</td>
                        <td>Column content</td>
                        <td>Column content</td>
                        <td>Column content</td>
                      </tr>
                      <tr>
                        <td>2</td>
                        <td>Column content</td>
                        <td>Column content</td>
                        <td>Column content</td>
                      </tr>
                      <tr class="table-active">
                        <td>3</td>
                        <td>Column content</td>
                        <td>Column content</td>
                        <td>Column content</td>
                      </tr>
                      <tr class="table-info">
                        <td>4</td>
                        <td>Column content</td>
                        <td>Column content</td>
                        <td>Column content</td>
                      </tr>
                      <tr class="table-info">
                        <td>5</td>
                        <td>Column content</td>
                        <td>Column content</td>
                        <td>Column content</td>
                      </tr>
                      <tr class="table-info">
                        <td>6</td>
                        <td>Column content</td>
                        <td>Column content</td>
                        <td>Column content</td>
                      </tr>
                      <tr class="table-warning">
                        <td>7</td>
                        <td>Column content</td>
                        <td>Column content</td>
                        <td>Column content</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
          <footer id="footer">
            <div class="row">
              <div class="col-lg-12">

                <ul class="list-unstyled">
                  <li class="float-lg-right"><a href="#top">Back to top</a></li>
                  <li><a href="https://twitter.com/smartaip">Twitter</a></li>
                  <li><a href="https://github.com/shakarbhattarai/SmartAIP/">GitHub</a></li>
                  <li><a href="#">API</a></li>
                </ul>
                <p>el 7th Sense</p>

              </div>
            </div>

          </footer>
        </div>

      </div>
    );
  }
}

export default App;
