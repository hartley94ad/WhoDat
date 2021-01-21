import React, {useState} from 'react'

import ArrowDropDownIcon from '@material-ui/icons/ArrowDropDown';
import IconButton from '@material-ui/core/IconButton'
import Menu from '@material-ui/core/Menu';
import { makeStyles } from '@material-ui/core';


const useStyles = makeStyles((theme) => ({
    unSelectable: {
        userSelect: 'none'
    }
}))

export const DropDownCell = (props) => {
    const classes = useStyles()
    const [anchorEl, setAnchorEl] = useState(null)

    const handleClick = (e) => {
        setAnchorEl(e.currentTarget)
    }

    const handleClose = () => {
        setAnchorEl(null)
    }

    const copyFriendly = props.copyFriendly || false

    return (
        <React.Fragment>
            {copyFriendly === false &&
                <React.Fragment>
                    <IconButton
                        aria-controls={`${props.friendly}-menu`}
                        onClick={handleClick}
                        size='small'
                    >
                        <ArrowDropDownIcon />
                    </IconButton>
                    {anchorEl !== null &&
                        <Menu
                            anchorEl={anchorEl}
                            keepMounted
                            open={Boolean(anchorEl)}
                            onClose={handleClose}
                        >
                            {props.children}
                        </Menu>
                    }
                </React.Fragment>
            }
            {props.value}
        </React.Fragment>

    )
}

export default DropDownCell