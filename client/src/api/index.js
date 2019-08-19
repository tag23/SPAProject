import axios from 'axios'

const API_URL = 'http://localhost:5000/api/v1'
// export function postNewSurvey (survey, jwt) {
//   return axios.post(`${API_URL}/surveys/`, survey, { headers: { Authorization: `Bearer: ${jwt}` } })
// }

export function authenticate(userData) {
    return axios.post(`${API_URL}/login`, userData)
}

export function register(userData) {
    console.log(userData)
    return axios.post(`${API_URL}/register`, userData)
}

export function getUserList(jwt) {
    return axios.get(`${API_URL}/get-users`, {headers: {Authorization: `Bearer: ${jwt}`}})
}

export function editUser(userData, jwt) {
    return axios.post(`${API_URL}/edit`, {
        headers: {
            Authorization: `Bearer: ${jwt}`,
        },
        data: userData
    })
}


export function deleteUser(userId, jwt) {
    return axios.get(`${API_URL}/delete`, {
        headers: {
            Authorization: `Bearer: ${jwt}`,
        },
        params: {
            user_id: userId
        }
    })

}