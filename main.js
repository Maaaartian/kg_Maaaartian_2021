function solution(s, t){
    if(s.length !== t.length) return false // compare length
    let map = new Map() // map to store intermediate mapping results
    for(i=0; i<s.length; i++){
        let key = s.charAt(i)
        // if a letter has appeared already and has been mapped to a new letter, return False
        if(map.get(key) !== undefined && map.get(key) !== t.charAt(i)) return false
        map.set(key, t.charAt(i)) // update the map
    }
    return true
}

let result = solution(process.argv[2], process.argv[3])
console.log(result)