import React from "react";

import classes from "./Button.module.css";

export default function Button({ children, onClick, disabled, className }) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={`${classes.button} ${className && className}`}
    >
      {children}
    </button>
  );
}
