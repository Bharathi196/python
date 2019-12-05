import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Test} from './test'
import { observable, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TestService {

  constructor(private http:HttpClient) {}
    getData():Observable<any>{
      //return this.http.get('/assets/json/data.json');
      return this.http.get('https://jsonplaceholder.typicode.com/posts/1/comments');
     // return this.http.get('/assets/json/data.json');
    } 

  }










  