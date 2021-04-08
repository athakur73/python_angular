import {Injectable} from '@angular/core';
 import {HttpClient, HttpErrorResponse} from '@angular/common/http';
 import {Observable, throwError} from 'rxjs';
 import { catchError, map, tap } from 'rxjs/operators';
import {API_URL} from '../env';

@Injectable()
export class projectsApiService {
    public employeesList: any;
  constructor(private http: HttpClient) {
  }
  getProjects() {
    return this.http.get(`${API_URL}/projects`);
}

}