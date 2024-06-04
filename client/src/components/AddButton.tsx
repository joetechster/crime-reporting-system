import React from "react";
import { makeStyles } from "@mui/styles";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";
import DialogForm from "./NewReportDialog";

const useStyles = makeStyles((theme) => ({
  root: {
    position: "fixed",
    bottom: 16,
    right: 16,
  },
}));

export default function AddButton() {
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <>
      <div className={classes.root}>
        <Fab color="primary" aria-label="add" onClick={handleClickOpen}>
          <AddIcon />
        </Fab>
      </div>
      <DialogForm open={open} handleClose={handleClose} title="Add New Report" />
    </>
  );
}
