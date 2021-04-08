import { Component, OnInit } from '@angular/core';
import {  FormGroup,FormControl } from '@angular/forms';
@Component({
  selector: 'app-add-projects',
  templateUrl: './add-projects.component.html',
  styleUrls: ['./add-projects.component.css']
})
export class AddProjectsComponent implements OnInit {
  profileForm = new FormGroup({
    clientname: new FormControl(''),
    projectcode: new FormControl(''),
    projectname: new FormControl(''),
    projectstartdate: new FormControl(''),
    projectstatus: new FormControl(''),
    billingtype: new FormControl(''),
    segment: new FormControl(''),
    geography: new FormControl(''),
    solutioncategory: new FormControl(''),
    financialyear: new FormControl(''),
        
  });
  constructor() { }

  ngOnInit(): void {
  }
  onSubmit() {
    // TODO: Use EventEmitter with form value
    
    console.warn(this.profileForm.value);
  }
}
