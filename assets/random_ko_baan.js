const getRandomExclusive = (min, max) => {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const getRandomVal = (obj) => {
    keys = Object.keys(obj)
    keylen = keys.length
    rand = getRandomExclusive(0, keylen - 1)
    console.log(rand, keylen)
    return obj[keys[rand]]
}
const getRandomIndex = (arr) => {
    len = arr.length
    rand = getRandomExclusive(0, len - 1)
    return arr[rand]
}

const getRandomFirstName = (param) => {
    if (param === 'boy') {
        fnames = first_names.boy
    } else if (param === 'girl') {
        fnames = first_names.girl
    } else {
        // 50% Chance to be a boy or a girl 
        // 25% chance to be half boy half girl
        fnames = (Math.floor(Math.random() * 2) == 0) ? first_names.boy : first_names.girl
    }
    return getRandomIndex(getRandomVal(fnames))
}

function* times(n) {
    for (let i = 0; i < n; i++)
        yield i;
}