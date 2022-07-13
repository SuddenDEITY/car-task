import React from "react";
import './styles.css';

function TableExtra({detail}){
    const extras = detail.extras;
    return (
        <tr>
            <td>
                <div className="accordion" id="accordionExample3">
                    {extras.map(extra => 
                        <div className="accordion-item" key={extra.id}>
                        <h2 id={`heading${detail.id}${extra.id}bc`} className="accordion-header">
                            <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target={`#collapse${detail.id}${extra.id}bc`} aria-expanded="true" aria-controls={`collapse${detail.id}${extra.id}bc`}>
                                Дополнение {extra.id}
                            </button>
                            </h2>
                            <div id={`collapse${detail.id}${extra.id}bc`} className="accordion-collapse collapse hide" aria-labelledby={`heading${detail.id}${extra.id}bc`} data-bs-parent="#accordionExample3">
                            <div className="accordion-body">
                                <table>
                                    <tbody>
                                        <tr className="extra">
                                            <th>{extra.detail_key}</th>
                                            <td>{extra.detail_value}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            </div>
                        </div>
                    )}
                </div>
            </td>
        </tr>
    )
}

function TableDetail({car}){
    const details = car.details;
    return (
       <>
             <div className="accordion" id="accordionExample2">
                                        {details.map((detail => 
                                            <div className="accordion-item" key={detail.id}>
                                            <h2 id={`heading${car.id}${detail.id}`} className="accordion-header">
                                                <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target={`#collapse${car.id}${detail.id}`} aria-expanded="true" aria-controls={`collapse${car.id}${detail.id}`}>
                                                    {detail.detail_type.type_name}
                                                </button>
                                                </h2>
                                                <div id={`collapse${car.id}${detail.id}`} className="accordion-collapse collapse hide" aria-labelledby={`heading${car.id}${detail.id}`} data-bs-parent="#accordionExample2">
                                                <div className="accordion-body">
                                                    <table>
                                                        <thead>
                                                            <tr  className="detail">
                                                                <th>Стоимость детали</th>
                                                                <td>{detail.price}</td>
                                                            </tr>
                                                            <tr className="detail">
                                                                <th>Количество деталей</th>
                                                                <td>{detail.quantity}</td>
                                                            </tr>
                                                            <tr className="detail">
                                                                <th>Общая стоимость деталей</th>
                                                                <td>{detail.total_price}</td>
                                                            </tr>
                                                        </thead>
                                                        <tbody>
                                                            {detail.extras ? <TableExtra detail={detail}/> : <></>}
                                                        </tbody>
                                                    </table>
                                                </div>
                                                </div>
                                        </div>))}
                                        </div>
       </>
    )
}

function Table({items}) {
    return (
        <>
        <div className="accordion" id="accordionExample1">
            {items.map(car => 
            <div className="accordion-item" key={car.id}>
                <h2 id={`heading${car.id}`} className="accordion-header">
                <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target={`#collapse${car.id}`} aria-expanded="true" aria-controls={`collapse${car.id}`}>
                    {car.name}
                </button>
                </h2>
                <div id={`collapse${car.id}`} className="accordion-collapse collapse hide" aria-labelledby={`heading${car.id}`} data-bs-parent="#accordionExample1">
                    <div className="accordion-body">
                        <table>
                            <thead>
                                <tr className="car">
                                    <th>Стоимость</th>
                                    <td>{car.price}</td>
                                </tr>
                                <tr className="car">
                                    <th>Наценка производителя</th>
                                    <td>{car.manufacturer_charge} %</td>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        <TableDetail car={car}/>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            )}
        </div> 
        </>
    )
}

export default Table;
