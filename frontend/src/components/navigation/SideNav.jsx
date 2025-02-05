import React from "react";

import classes from "./SideNav.module.css";
import Button from "../custom-ux/Button";
import { IoMenu } from "react-icons/io5";

export default function SideNav({ expandSideNav, setExpandSideNav }) {
  function expandHandler() {
    setExpandSideNav(!expandSideNav);
  }

  return (
    <div
      className={`${classes.sideNav} ${
        expandSideNav && classes.expandedSideNav
      }`}
    >
      <Button onClick={expandHandler} className={classes.menuButton}>
        <IoMenu />
        {/* Click to {expandSideNav ? "Shrink" : "Expand"} */}
      </Button>
      SideNav
    </div>
  );
}
