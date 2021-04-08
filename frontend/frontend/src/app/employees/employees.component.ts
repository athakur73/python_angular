import { Component, OnInit } from '@angular/core';
import {Subscription} from 'rxjs';
import {employeesApiService} from './employees.service';

@Component({
  selector: 'app-employees',
  templateUrl: './employees.component.html',
  styleUrls: ['./employees.component.css']
})
export class EmployeesComponent implements OnInit {
  public employee_list: any;
  empListSubs: Subscription;
  constructor(private empApi: employeesApiService) { }

  ngOnInit()  {
    this.empListSubs = this.empApi
                            .getExams()
                            .subscribe(res=>{this.employee_list=res;console.log(res)},console.error) ;
  }

}
