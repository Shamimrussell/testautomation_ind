import http from 'k6/http';
import { check } from 'k6';

export default function () {
    const res = http.get('https://souderbroder-loan-lab.lovable.app');
    check(res, {
        'status is 200': (r) => r.status === 200,
    });
}