import React, { useState } from "react";
import { Outlet } from "react-router-dom";
import TopNav from "../components/navigation/TopMenuBar";
import SideNav from "../components/navigation/SideNav";

import classes from "./RootLayout.module.css";

export default function RootLayout() {
  const [expandSideNav, setExpandSideNav] = useState(true);

  return (
    <>
      <TopNav />

      <SideNav
        expandSideNav={expandSideNav}
        setExpandSideNav={setExpandSideNav}
      />

      <main
        className={expandSideNav ? classes.shrunkMain : classes.expandedMain}
      >
        <Outlet />
      </main>
    </>
  );
}
