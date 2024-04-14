const Row = (props) => {
    return(
        <tr>
            <td>{props.item.task}</td>
            <td>{props.item.deadline}</td>
            <td>{props.item.device}</td>
        </tr>
    )
}

export default Row;