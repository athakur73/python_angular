import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ExamsComponent } from './exams/exams.component';

const routes: Routes = [
  // { path: '', redirectTo: 'home', pathMatch: 'full'},
  { path: 'exams', component: ExamsComponent },
  // { path: 'route', component: ExamsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
