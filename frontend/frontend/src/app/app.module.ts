import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { ExamsComponent } from './exams/exams.component';
import { ExamsApiService } from './exams/exams.service';
import { EmployeesComponent } from './employees/employees.component';
import { employeesApiService } from './employees/employees.service';
import { AddEmployeeComponent } from './add-employee/add-employee.component';
import { ViewProjectsComponent } from './projects/view-projects.component';
import { AddProjectsComponent } from './add-projects/add-projects.component';
import { AssignProjectResourceComponent } from './assign-project-resource/assign-project-resource.component';
import { AssignResourceProjectComponent } from './assign-resource-project/assign-resource-project.component';
@NgModule({
  declarations: [
    AppComponent,
    ExamsComponent,
    EmployeesComponent,
    AddEmployeeComponent,
    ViewProjectsComponent,
    AddProjectsComponent,
    AssignProjectResourceComponent,
    AssignResourceProjectComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [ExamsApiService,employeesApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
