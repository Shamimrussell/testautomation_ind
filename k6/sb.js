// Import the http module to make HTTP requests. From this point, you can use `http` methods to make HTTP requests.
import http from 'k6/http';

// Import the sleep function to introduce delays. From this point, you can use the `sleep` function to introduce delays in your test script.
import { sleep } from 'k6';

const BASE_URL = 'https://souderbroder-loan-lab.lovable.app';
const API_KEY = 'API_KEY';

export const options = {
    // Define the number of iterations for the test
    iterations: 10,
    thresholds: {
        'http_req_duration{name:create_loan}': ['p(95)<2000'], // acceptanskriterium. 95% av alla request ska vara snabbare än 2000ms
    }

};

// The default exported function is gonna be picked up by k6 as the entry point for the test script. It will be executed repeatedly in "iterations" for the whole duration of the test.
export default function () {
    const headers = {
    'x-api-key': 'API_KEY',
    'Content-Type': 'application/json',
     };

  const payload = JSON.stringify({
    first_name: 'Test',
    last_name: 'Testsson',
    personal_number: '189001069815',
    email: 'test@example.com',
    loan_amount: '50000',
    employment_type: 'employed',
  });

    
  // Make a POST request to the target URL with headers and payload
  http.post(BASE_URL + '/partner-loan-api', payload, { headers, tags: { name: 'create_loan' } });
  
  // Sleep for 1 second to simulate real-world usage
  sleep(1);
}