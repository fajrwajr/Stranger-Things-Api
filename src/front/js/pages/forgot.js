import React, { useState, useEffect, useContext } from "react";
import PropTypes from "prop-types";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import { TextField } from "@material-ui/core";

export const Forgot = () => {
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const params = useParams();

  return (
    <>
      <div class="form-gap"></div>
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-md-4 col-md-offset-4">
            <div class="panel panel-default">
              <div class="panel-body">
                <div class="text-center">
                  <div>
                    <br></br>
                  </div>
                  <h3>
                    <i class="fa fa-lock fa-4x"></i>
                  </h3>
                  <h3 class="text-center">Forgot your password?</h3>
                  <p>You can reset it here.</p>
                  <div class="panel-body">
                    <form
                      id="register-form"
                      role="form"
                      autocomplete="off"
                      class="form"
                      method="post"
                    >
                      <div class="form-group">
                        <div class="input-group">
                          <span class="input-group-addon">
                            <i class="glyphicon glyphicon-envelope color-blue"></i>
                          </span>
                          <input
                            id="email"
                            onChange={(e) => setEmail(e.target.value)}
                            name="email"
                            placeholder="email address"
                            class="form-control"
                            type="email"
                          />
                        </div>
                      </div>
                      <div class="form-group text-center mt-4">
                        <input
                          name="recover-submit"
                          class="btn btn-lg btn-primary btn-block"
                          value="Reset Password"
                          type="submit"
                        />
                      </div>

                      <input
                        type="hidden"
                        class="hide"
                        name="token"
                        id="token"
                        value=""
                      />
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
