
import axios from 'axios'
const API_URL = process.env.API_URL

export default {
  API_URL: API_URL,
  get_wrapper: function (url, params = {}, headers = {'Content-Type': 'application/json'}) {
    return axios.get(
      API_URL + url,
      {
        params: params,
        headers: headers
      }
    ).catch(err => {
      console.log('you got error:', err)
    })
  }
}
