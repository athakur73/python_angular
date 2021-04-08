import { Component, OnInit } from '@angular/core';
import {Subscription} from 'rxjs';
import { projectsApiService } from './projects.services';
@Component({
  selector: 'app-view-projects',
  templateUrl: './view-projects.component.html',
  styleUrls: ['./view-projects.component.css']
})
export class ViewProjectsComponent implements OnInit {
  public project_list: any;
  projectListSubs: Subscription;
  constructor(private projectApi: projectsApiService) { }

  ngOnInit(): void {
    this.projectListSubs = this.projectApi
                            .getProjects()
                            .subscribe(res=>{this.project_list=res;console.log(res)},console.error) ;
  }

}
