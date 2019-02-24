// Global variables are bad
first_names = {}
last_names = {}

const main = async () => {
    const requests = {
        bfirst: await fetch('./first-names/b.json'),
        gfirst: await fetch('./first-names/g.json'),
        clasts: await fetch('./last-names/l.json'),
    }
    const response = {
        boy: await requests.bfirst.json(),
        girl: await requests.gfirst.json(),
        last: await requests.clasts.json(),
    }
    first_names.boy = response.boy
    first_names.girl = response.girl
    last_names = response.last

}