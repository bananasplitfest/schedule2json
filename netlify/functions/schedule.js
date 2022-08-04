const fetch = require('node-fetch')

function localToUTC(dt) {
    try {
        datePeriod = dt.split(" ")
        timePeriod = datePeriod[1].split(":")
        if ( datePeriod[2] === "PM" && timePeriod[0] !== "12" )
            timePeriod[0] = (parseInt(timePeriod[0]) + 12).toString()
        return datePeriod[0] + "T" + timePeriod[0].padStart(2, '0') + ":" + timePeriod[1].padStart(2, '0')
    } catch (error) {
        return false
    }
}

function strToBool(s)
{
    // will match one and only one of the string 'true','1', or 'on' rerardless
    // of capitalization and regardless off surrounding white-space.
    //
    regex=/^\s*(true|1|on)\s*$/i

    return regex.test(s);
}

function parseBool(b) {
    return !(/^(false|0)$/i).test(b) && !!b;
}

exports.handler = async function () {
    const SCHEDULE_DOC = 'https://opensheet.elk.sh/1YWymQHAIQnXhGOttbI20zflXY0HVfrvQ2yMcTWjtscw/Activities'
    
    const response = await fetch(SCHEDULE_DOC)
    const data = await response.json()

    const formattedData = []

    for( const key in data ) {
        const activity = {}
        activity.title = data[key]?.title ?? false
        activity.start = localToUTC(data[key].start)
        activity.end = localToUTC(data[key].end)
        activity.resourceId = data[key]?.location ?? "invalid"
        activity.description = data[key]?.description ?? false
        activity.pre = data[key]?.pre ?? false
        activity.post = data[key]?.post ?? false
        activity.highlight = data[key]?.highlight ?? false
        activity.entertainer = data[key]?.isEntertainer ?? false
        activity.activity = data[key]?.isActivity ?? false
        activity.link = data[key]?.link ?? false
        activity.genre = data[key]?.genre ?? false
        activity.buttons = []
        if ( data[key].button1 ) activity.buttons.push({
            title: data[key].button1,
            link: data[key].button1link
        })
        if ( data[key].button2 ) activity.buttons.push({
            title: data[key].button2,
            link: data[key].button2link
        })
        activity.image = {}
        if ( data[key].pageImage ) activity.image.page = {
            type: "page",
            file: data[key].pageImage,
            alt: data[key].pageImageAlt
        }
        if ( data[key].scheduleImage ) activity.image.schedule = {
            type: "schedule",
            file: data[key].scheduleImage,
            alt: data[key].scheduleImageAlt
        }
        activity.links = []
        if ( data[key].website ) activity.links.push({
            type: "website",
            link: data[key].website
        })
        if ( data[key].facebook ) activity.links.push({
            type: "facebook",
            link: data[key].facebook
        })
        if ( data[key].instagram ) activity.links.push({
            type: "instagram",
            link: data[key].instagram
        })
        if ( data[key].twitter ) activity.links.push({
            type: "twitter",
            link: data[key].twitter
        })
        if ( data[key].spotify ) activity.links.push({
            type: "spotify",
            link: data[key].spotify
        })
        if ( data[key].youtube ) activity.links.push({
            type: "youtube",
            link: data[key].youtube
        })
        if ( data[key].appleMusic ) activity.links.push({
            type: "appleMusic",
            link: data[key].appleMusic
        })
        if ( data[key].tiktok ) activity.links.push({
            type: "tiktok",
            link: data[key].tiktok
        })

        if ( activity.image && Object.keys(activity.image).length === 0 && Object.getPrototypeOf(activity.image) === Object.prototype ) delete activity.image
        if ( activity.buttons.length == 0 ) delete activity.buttons
        if ( activity.links.length == 0 ) delete activity.links

        for ( const k in activity ) {
            if ( activity[k] === "" || activity[k] === false ) delete activity[k]
            if ( activity[k] === "TRUE" ) activity[k] = true
        }

        formattedData.push(activity)
    }

    return {
        statusCode: 200,
        // body: 'Hello Banana'
        headers: {
            "Access-Control-Allow-Origin": "*", // Allow from anywhere 
        },
        body: JSON.stringify({
            activities: formattedData
        })
    }
}