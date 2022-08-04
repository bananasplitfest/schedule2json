const fetch = require('node-fetch')

exports.handler = async function () {
    const LOCATION_DOC = 'https://opensheet.elk.sh/1YWymQHAIQnXhGOttbI20zflXY0HVfrvQ2yMcTWjtscw/Locations'

    const response = await fetch(LOCATION_DOC)
    const data = await response.json()

    return {
        statusCode: 200,
        headers: {
            "Access-Control-Allow-Origin": "*", // Allow from anywhere 
        },
        body: JSON.stringify(data)
    }
}