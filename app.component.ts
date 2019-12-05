import { Component } from '@angular/core';
import { TestService } from './test.service';
import { Test } from './test'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  getData(): any {
    throw new Error("Method not implemented.");
  }
  data: any = [
    
  ]
  // author = {
  //   "userId": '',
  //   "id": '',
  //   "title":'',
  //   "body": ''
  // }
  abc:Test[];
  constructor(public testService: TestService) { }

  ngOnInit() {
    
    this.testService.getData().subscribe(
      data=>{
        this.abc=data;
      }
    );
  }
  /* method to call get-api from app.service */
  
  
  //title = 'example';
}
